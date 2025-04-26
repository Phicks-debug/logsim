from logsim import CustomLogger

log = CustomLogger(use_json=True, name="json_example")
log.debug("This is a DEBUG message")
log.info("This is an INFO message")
log.warning("This is a WARNING message")
log.error("This is an ERROR message")
log.critical("This is a CRITICAL message")
