import logging
import warnings

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

class CustomFormatter(logging.Formatter):
    def format(self, record):
        record.combined = f"[{record.filename}:{record.lineno}]".ljust(30)
        return super().format(record)
# make the logger look nicer with a config
formatter = CustomFormatter("%(combined)s  %(message)s")
channel = logging.StreamHandler()
channel.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[channel])

warnings.simplefilter(action='ignore', category=FutureWarning)

sys_logger = logging.getLogger(__name__)


