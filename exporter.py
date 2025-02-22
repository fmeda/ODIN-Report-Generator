import pandas as pd
import os
from utils.logger import log_info, log_error

def export_to_csv(data, output_dir):
    try:
        df = pd.DataFrame(data)
        output_file = os.path.join(output_dir, "report.csv")
        df.to_csv(output_file, index=False)
        log_info(f"Report saved to {output_file}")
    except Exception as e:
        log_error(f"Error exporting to CSV: {str(e)}")

def export_to_powerbi(data, output_dir):
    output_file = os.path.join(output_dir, "powerbi_report.csv")
    export_to_csv(data, output_dir)
    log_info(f"Power BI report saved to {output_file}")
