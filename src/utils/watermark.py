from src.utils.constants import WATERMARK_LOCATION, WATERMARK_TABLE_COLUMNS
from src.utils.files import save_file
from src.utils.logger import sys_logger
import pandas as pd


def get_watermark_table():
    sys_logger.info(f"Reading watermark table from {WATERMARK_LOCATION}")
    try:
        table = pd.read_parquet(WATERMARK_LOCATION)
    except FileNotFoundError:
        sys_logger.warning(f"Watermark table not found at {WATERMARK_LOCATION}. Creating new table")
        table = pd.DataFrame(columns=WATERMARK_TABLE_COLUMNS)
    sys_logger.info(f"Watermark table has {len(table)} rows")
    return table

def get_last_run_date(source_name, watermark):
    sys_logger.info(f"Getting last run date for {source_name}")
    last_run = watermark[watermark['source'] == source_name]
    if len(last_run) == 0:
        sys_logger.info(f"No previous runs found for {source_name}")
        return None
    last_run_date = last_run['file_date'].max()
    sys_logger.info(f"Last run date for {source_name} is {last_run_date}")
    return pd.to_datetime(last_run_date)

def update_watermark_table(watermark, stats):
    #  stats = {
    #     "source": source_name,
    #     "filename": source_name,
    #     "processed_rows": len(clean_records),
    #     "error_rows": len(error_records),
    #     "process_time": pd.Timestamp.now(),
    #     "file_date": date,
    #     "file_id": str(uuid4()),
    # }

    sys_logger.info(f"Updating watermark table with {stats}")
    watermark = pd.concat([watermark, pd.DataFrame([stats])])
    sys_logger.info(f"Watermark table now has {len(watermark)} rows")
    save_file(WATERMARK_LOCATION, watermark)
    sys_logger.info(f"Watermark table saved to {WATERMARK_LOCATION}")
    return watermark