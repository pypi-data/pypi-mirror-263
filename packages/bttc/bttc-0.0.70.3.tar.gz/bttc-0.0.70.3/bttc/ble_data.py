"""Module to hold dataclass or related data used in Bluetooth BLE."""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ActiveGroupInfo:
  currentlyActiveGroupId: int | None = None
  mActiveAudioOutDevice: str | None = None
  mActiveAudioInDevice: str | None = None
  mUnicastGroupIdDeactivatedForBroadcastTransition: int | None = None
  mExposedActiveDevice: str | None = None
  mHfpHandoverDevice: Any | None = None
  mLeAudioIsInbandRingtoneSupported: str | None = None
  others: dict[str, str] = field(default_factory=dict)


@dataclass
class GroupInfo:
  Group: str | None = None
  isActive: str | None = None
  isConnected: str | None = None
  mDirection: int | None = None
  grouplead: str | None = None
  others: dict[str, str] = field(default_factory=dict)


@dataclass
class LeAudioStateMachine:
  totalrecords: int | None = None
  others: dict[str, str] = field(default_factory=dict)


@dataclass
class StateMachineLog:
  le_audio_state_machine_list: list[LeAudioStateMachine] = field(
    default_factory=list)
  curState: str | None = None
  mDevInbandRingtoneEnabled: bool | None = None
  mSinkAudioLocation: int | None = None
  mDirection: int | None = None
  others: dict[str, str] = field(default_factory=dict)


@dataclass
class DeviceInfo:
  mDevice: str | None = None
  StateMachine: str | None = None
  state_machine_list: list[StateMachineLog] = field(default_factory=list)
  others: dict[str, str] = field(default_factory=dict)


@dataclass
class LeAudioService:
  isDualModeAudioEnabled: str | None = None
  active_group_list: list[ActiveGroupInfo] = field(default_factory=list)
  group_list: list[GroupInfo] = field(default_factory=list)
  device_list: list[DeviceInfo] = field(default_factory=list)
  others: dict[str, str] = field(default_factory=dict)
