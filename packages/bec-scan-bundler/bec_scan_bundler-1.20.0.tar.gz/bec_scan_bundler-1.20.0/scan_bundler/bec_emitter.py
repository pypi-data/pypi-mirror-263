from __future__ import annotations

from typing import TYPE_CHECKING

from bec_lib import MessageEndpoints, bec_logger, messages

from .emitter import EmitterBase

logger = bec_logger.logger

if TYPE_CHECKING:
    from .scan_bundler import ScanBundler


class BECEmitter(EmitterBase):
    def __init__(self, scan_bundler: ScanBundler) -> None:
        super().__init__(scan_bundler.connector)
        self.scan_bundler = scan_bundler

    def on_scan_point_emit(self, scanID: str, pointID: int):
        self._send_bec_scan_point(scanID, pointID)

    def on_baseline_emit(self, scanID: str):
        self._send_baseline(scanID)

    def _send_bec_scan_point(self, scanID: str, pointID: int) -> None:
        sb = self.scan_bundler

        info = sb.sync_storage[scanID]["info"]
        msg = messages.ScanMessage(
            point_id=pointID,
            scanID=scanID,
            data=sb.sync_storage[scanID][pointID],
            metadata={
                "scanID": scanID,
                "scan_type": info.get("scan_type"),
                "scan_report_devices": info.get("scan_report_devices"),
            },
        )
        self.add_message(
            msg,
            MessageEndpoints.scan_segment(),
            MessageEndpoints.public_scan_segment(scanID=scanID, pointID=pointID),
        )

    def _send_baseline(self, scanID: str) -> None:
        sb = self.scan_bundler

        msg = messages.ScanBaselineMessage(
            scanID=scanID,
            data=sb.sync_storage[scanID]["baseline"],
            metadata=sb.sync_storage[scanID]["info"],
        )
        pipe = sb.connector.pipeline()
        sb.connector.set(
            MessageEndpoints.public_scan_baseline(scanID=scanID), msg, expire=1800, pipe=pipe
        )
        sb.connector.set_and_publish(MessageEndpoints.scan_baseline(), msg, pipe=pipe)
        pipe.execute()
