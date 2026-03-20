"""Helix — Open-Source Modular AI Home Assistant."""

import asyncio
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("helix")


async def main():
    logger.info("Helix starting…")

    # Phase 1: these imports will be uncommented as each module is built
    # from src.helix_voice.pipeline import VoicePipeline
    # from src.helix_mind.llm import LLMEngine
    # from src.helix_hal.device_manager import DeviceManager

    logger.info("All systems nominal. Waiting for wake word…")

    # Placeholder — keeps the process alive until pipeline is wired
    try:
        await asyncio.Event().wait()
    except KeyboardInterrupt:
        logger.info("Helix shutting down.")


if __name__ == "__main__":
    asyncio.run(main())