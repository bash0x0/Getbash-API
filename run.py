import main
import uvicorn
import sys
import traceback
import logging

# Configuration File
import config as cfg

log_config = uvicorn.config.LOGGING_CONFIG
log_config["formatters"]["access"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"

if __name__ == '__main__':
    print(f'Starting API Server: {cfg.api["host"]}:{cfg.api["port"]}\n')

    try:
        uvicorn.run(
            "main:app",
            host=cfg.api["host"],
            port=cfg.api["port"],
            workers=cfg.api["workers"],
            log_level=cfg.api["log_level"],
            log_config=log_config,
            reload=cfg.api["reload"],
            debug=cfg.api["debug"]
        )
    except KeyboardInterrupt:
        print(f'\nExiting\n')
    except Exception as e:
        print(f'Failed to Start API')
        print('='*100)
        traceback.print_exc(file=sys.stdout)
        print('='*100)
        print('Exiting\n')
    print(f'\n\n')
