from enum import Enum
from typing import List, Union

# Enums
class WorldEventType(Enum):
    Init = 0
    Sync = 1
    WorldInfoUpdate = 10
    Notification = 11
    WorldReset = 12
    Block = 13
    Add = 20
    Leave = 21
    PlayerReset = 22
    Chat = 23
    SmileyChange = 24
    AuraChange = 25
    CanEditChange = 26
    CanUseGodModeChange = 27
    Move = 40
    MoveUpdate = 41
    Death = 42
    SetRespawnPoint = 43
    Respawn = 44
    MapEnablerTouch = 50
    GodModeEnablerTouch = 51
    TrophyTouch = 52
    CoinCollect = 53
    KeyTouch = 54
    CrownTouch = 55
    PurpleSwitchTouch = 56
    OrangeSwitchTouch = 57
    CheckpointTouch = 58
    EffectTouch = 59
    PlayerTouch = 60
    TeamChange = 61

class WorldPerm(Enum):
    PermPlayer = 0
    PermEdit = 1
    PermCommands = 2
    PermOwner = 3

class WorldInfoFields(Enum):
    Undefined = 0
    Title = 1
    Map = 2

class CoinType(Enum):
    CoinGold = 0
    CoinBlue = 1

class KeyType(Enum):
    KeyRed = 0
    KeyGreen = 1
    KeyBlue = 2
    KeyMagenta = 3
    KeyYellow = 4
    KeyCyan = 5

class EffectType(Enum):
    None = 0
    Jump = 1
    Speed = 2
    Gravity = 3
    Levitation = 4
    MultiJump = 5
    GravityDirection = 6
    OnFire = 7
    Invulnerability = 8
    Poison = 9
    Zombie = 10
    Curse = 11

class Team(Enum):
    TeamNone = 0
    TeamRed = 1
    TeamGreen = 2
    TeamBlue = 3
    TeamMagenta = 4
    TeamYellow = 5
    TeamCyan = 6

# Messages
class JoinWorld:
    def __init__(self, auth_token: str = '', world_id: str = ''):
        self.auth_token = auth_token
        self.world_id = world_id

class WorldInfo:
    def __init__(self, width: int = 0, height: int = 0, deflated_world_data: bytes = b'',
                 owner_id: str = '', owner_name: str = '', updated_fields: WorldInfoFields = WorldInfoFields.Undefined,
                 world_title: str = '', map_hidden: bool = False):
        self.width = width
        self.height = height
        self.deflated_world_data = deflated_world_data
        self.owner_id = owner_id
        self.owner_name = owner_name
        self.updated_fields = updated_fields
        self.world_title = world_title
        self.map_hidden = map_hidden

class WorldResetArgs:
    def __init__(self, deflated_world_data: bytes = b'', respawn_point: 'Vector2U' = None):
        self.deflated_world_data = deflated_world_data
        self.respawn_point = respawn_point

class WorldData:
    def __init__(self, block_entries: List['BlockEntry'] = None):
        self.block_entries = block_entries if block_entries is not None else []

class BlockEntry:
    def __init__(self, xs: bytes = b'', ys: bytes = b'', block_id: int = 0,
                 layer: 'BlockLayer' = None, int_args: List[int] = None, string_args: List[str] = None):
        self.xs = xs
        self.ys = ys
        self.block_id = block_id
        self.layer = layer
        self.int_args = int_args if int_args is not None else []
        self.string_args = string_args if string_args is not None else []

class PlayerInfo:
    def __init__(self, local_player_id: int = 0, player_id: str = '', name: str = '',
                 smiley_id: int = 0, aura_shape_id: int = 0, aura_color_id: int = 0,
                 is_ready: bool = False, last_position_update: int = 0,
                 play_state: 'PlayerState' = None, perm_level: WorldPerm = WorldPerm.PermPlayer,
                 can_edit: bool = False):
        self.local_player_id = local_player_id
        self.player_id = player_id
        self.name = name
        self.smiley_id = smiley_id
        self.aura_shape_id = aura_shape_id
        self.aura_color_id = aura_color_id
        self.is_ready = is_ready
        self.last_position_update = last_position_update
        self.play_state = play_state
        self.perm_level = perm_level
        self.can_edit = can_edit

class PlayerResetArgs:
    def __init__(self, respawn_point: 'Vector2U' = None, target_local_player_id: int = 0):
        self.respawn_point = respawn_point
        self.target_local_player_id = target_local_player_id

class PlayerState:
    def __init__(self, move_args: 'MoveArgs' = None, respawn_point: 'Vector2U' = None,
                 completed_level: bool = False, map_unlocked: bool = False,
                 god_mode_unlocked: bool = False, deaths: int = 0,
                 coin_states: List['CoinState'] = None, enabled_purple_switches: List[int] = None,
                 effects: List['EffectState'] = None, team: Team = Team.TeamNone):
        self.move_args = move_args
        self.respawn_point = respawn_point
        self.completed_level = completed_level
        self.map_unlocked = map_unlocked
        self.god_mode_unlocked = god_mode_unlocked
        self.deaths = deaths
        self.coin_states = coin_states if coin_states is not None else []
        self.enabled_purple_switches = enabled_purple_switches if enabled_purple_switches is not None else []
        self.effects = effects if effects is not None else []
        self.team = team

class CanUseGodModeChangeArgs:
    def __init__(self, can_use_god_mode: bool = False):
        self.can_use_god_mode = can_use_god_mode

class CanEditChangeArgs:
    def __init__(self, can_edit: bool = False):
        self.can_edit = can_edit

class MoveArgs:
    def __init__(self, tick_delta: int = 0, seed: int = 0, position: 'Vector2D' = None,
                 direction: 'Vector2I' = None, velocity: 'Vector2D' = None,
                 is_jumping: bool = False, is_god: bool = False):
        self.tick_delta = tick_delta
        self.seed = seed
        self.position = position
        self.direction = direction
        self.velocity = velocity
        self.is_jumping = is_jumping
        self.is_god = is_god

class Vector2U:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

class Vector2I:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

class Vector2D:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

class SmileyChangeArgs:
    def __init__(self, smiley_id: int = 0):
        self.smiley_id = smiley_id

class AuraChangeArgs:
    def __init__(self, aura_shape_id: int = 0, aura_color_id: int = 0):
        self.aura_shape_id = aura_shape_id
        self.aura_color_id = aura_color_id

class ChatArgs:
    def __init__(self, message: str = '', is_private: bool = False,
                 target_local_player_id: int = 0):
        self.message = message
        self.is_private = is_private
        self.target_local_player_id = target_local_player_id

class NotificationArgs:
    def __init__(self, message: str = ''):
        self.message = message

class BlockArgs:
    def __init__(self, x: int = 0, y: int = 0, block_id: int = 0,
                 layer: 'BlockLayer' = None, int_args: List[int] = None,
                 string_args: List[str] = None):
        self.x = x
        self.y = y
        self.block_id = block_id
        self.layer = layer
        self.int_args = int_args if int_args is not None else []
        self.string_args = string_args if string_args is not None else []

class DeathArgs:
    def __init__(self, tick_delta: int = 0, count: int = 0):
        self.tick_delta = tick_delta
        self.count = count

class RespawnArgs:
    def __init__(self, tick_delta: int = 0, position: 'Vector2D' = None):
        self.tick_delta = tick_delta
        self.position = position

class CoinState:
    def __init__(self, coin_type: CoinType = CoinType.CoinGold, coin_amount: int = 0,
                 collected_coins_positions: List[Vector2U] = None):
        self.coin_type = coin_type
        self.coin_amount = coin_amount
        self.collected_coins_positions = collected_coins_positions if collected_coins_positions is not None else []

class CoinCollectArgs:
    def __init__(self, tick_delta: int = 0, x: int = 0, y: int = 0, coin_type: CoinType = CoinType.CoinGold,
                 discard: bool = False, coin_amount: int = 0):
        self.tick_delta = tick_delta
        self.x = x
        self.y = y
        self.coin_type = coin_type
        self.discard = discard
        self.coin_amount = coin_amount

class KeyState:
    def __init__(self, key_type: KeyType = KeyType.KeyRed, last_activation: int = 0, duration: int = 0):
        self.key_type = key_type
        self.last_activation = last_activation
        self.duration = duration

class KeyTouchArgs:
    def __init__(self, tick_delta: int = 0, x: int = 0, y: int = 0, key_type: KeyType = KeyType.KeyRed,
                 duration: int = 0):
        self.tick_delta = tick_delta
        self.x = x
        self.y = y
        self.key_type = key_type
        self.duration = duration

class BlockTouchArgs:
    def __init__(self, tick_delta: int = 0, x: int = 0, y: int = 0):
        self.tick_delta = tick_delta
        self.x = x
        self.y = y

class SmileyChangingBlockTouchArgs:
    def __init__(self, tick_delta: int = 0, x: int = 0, y: int = 0, smiley_id: int = 0):
        self.tick_delta = tick_delta
        self.x = x
        self.y = y
        self.smiley_id = smiley_id

class SwitchTouchArgs:
    def __init__(self, tick_delta: int = 0, x: int = 0, y: int = 0, switch_id: int = 0, enabled: bool = False):
        self.tick_delta = tick_delta
        self.x = x
        self.y = y
        self.switch_id = switch_id
        self.enabled = enabled

class EffectState:
    def __init__(self, effect: EffectType = EffectType.None, int_arg: int = 0, time_activated: int = 0):
        self.effect = effect
        self.int_arg = int_arg
        self.time_activated = time_activated

class EffectTouchArgs:
    def __init__(self, tick_delta: int = 0, x: int = 0, y: int = 0, effect: EffectType = EffectType.None,
                 enable: bool = False, int_arg: int = 0):
        self.tick_delta = tick_delta
        self.x = x
        self.y = y
        self.effect = effect
        self.enable = enable
        self.int_arg = int_arg

class PlayerTouchArgs:
    def __init__(self, tick_delta: int = 0, local_player_id: int = 0, zombie: bool = False, curse: bool = False,
                 time_activated: int = 0, duration: int = 0):
        self.tick_delta = tick_delta
        self.local_player_id = local_player_id
        self.zombie = zombie
        self.curse = curse
        self.time_activated = time_activated
        self.duration = duration

class TeamChangeArgs:
    def __init__(self, tick_delta: int = 0, x: int = 0, y: int = 0, team: Team = Team.TeamNone):
        self.tick_delta = tick_delta
        self.x = x
        self.y = y
        self.team = team

class WorldEvent:
    def __init__(self, event_type: WorldEventType = WorldEventType.Init, issuer_local_player_id: int = 0,
                 event_args: Union[WorldInfo, NotificationArgs, WorldResetArgs, BlockArgs, PlayerInfo, PlayerResetArgs,
                                   ChatArgs, SmileyChangeArgs, AuraChangeArgs, CanEditChangeArgs,
                                   CanUseGodModeChangeArgs, MoveArgs, DeathArgs, RespawnArgs, BlockTouchArgs,
                                   CoinCollectArgs, KeyTouchArgs, SwitchTouchArgs, EffectTouchArgs, PlayerTouchArgs,
                                   TeamChangeArgs] = None):
        self.event_type = event_type
        self.issuer_local_player_id = issuer_local_player_id
        self.event_args = event_args
