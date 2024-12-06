SYSTEM_COLS = ["is_current", "expiry_date", "effective_from", "hash"]
WATERMARK_LOCATION = './watermark.parquet'
WATERMARK_TABLE_COLUMNS = ["source", 'file_name', 'processed_rows', 'error_rows', 'process_time', 'file_date', 'file_id']