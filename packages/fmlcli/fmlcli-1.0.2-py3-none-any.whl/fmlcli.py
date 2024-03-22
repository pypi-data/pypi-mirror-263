#!/usr/bin/env python3
import argparse
from glitter_sdk.client.lcd import LCDClient
from glitter_sdk.core import Numeric, Coins
from glitter_sdk.key.mnemonic import MnemonicKey
from glitter_sdk.util.parse_sql import prepare_sql
from glitter_sdk.util.parse_query_str import *
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.align import Align
from rich.tree import Tree
from glitter_sdk.util.highlight import *
from datetime import datetime


def format_file_size(size_bytes):
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes // 1024} KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes // (1024 * 1024)} MB"
    else:
        return f"{size_bytes / (1024 * 1024 * 1024):.2f} GB"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, required=True,
                        help='Please enter the desired file name for searching.')
    parser.add_argument('-n', '--number', type=int, default=10,
                        help='The number of results you would like to display.')
    args = parser.parse_args()

    mnemonic = ""
    mk = MnemonicKey(mnemonic)
    client = LCDClient(
        chain_id="glitter_12000-2",
        url="https://api.xian.glitter.link",
        gas_prices=Coins.from_str("1agli"),
        gas_adjustment=Numeric.parse(1.5))
    glitter_db_client = client.db(mk)
    query = args.file
    queries = [MatchQuery("file_name", query, 1.0)]
    query_str = query_string_prepare(queries)
    highlight = highlight_prepare(["file_name"])
    sql = prepare_sql(
        "select {} _id ,category ,file_name ,firstadd_utc_timestamp ,filesize ,total_count from library.dht where query_string_recency(%s) limit 0,".format(
            highlight), [query_str])
    sql = sql + str(args.number)
    rst = glitter_db_client.query(sql)
    console = Console()
    table = Table(show_header=True, header_style="bold magenta", expand=True)
    table_centered = Align.center(table)
    link = "The method of download via magnet link (https://anybt.eth.limo/#/guide)"
    table.add_column(link, no_wrap=True)
    table.add_column("ext", style="dim", no_wrap=True)

    for row in rst:
        ext = Tree("ext")
        timestamp_dt = datetime.utcfromtimestamp(row["firstadd_utc_timestamp"])
        format_timestamp = timestamp_dt.strftime("%Y-%m-%d")
        ext.add(format_timestamp)
        format_size = format_file_size(row["filesize"])
        ext.add(format_size)
        hot = str(int(row["total_count"])) + "Hot"
        ext.add(hot)
        ext.add(row["category"])
        content = Tree("content")
        content.add(row["_highlight_file_name"].replace("<mark>", "[red]").replace("</mark>", "[/red]"))
        magnet_link = "magnet:?xt=urn:btih:" + row["_id"]
        content.add(magnet_link)

        table.add_row(content, ext)

    console.print(table)


if __name__ == '__main__':
    main()
