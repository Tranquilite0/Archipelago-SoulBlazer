from collections import namedtuple
from dataclasses import dataclass
from typing import Optional, Callable
from enum import Enum
from BaseClasses import Region, Location, Entrance, Item, ItemClassification
from .Rules import RuleFlag, get_rule_for_location
from .Names import LairID, LairName, ChestID, ChestName, NPCRewardID, NPCRewardName
from .Names.ArchipelagoID import BASE_ID, LAIR_ID_OFFSET, NPC_REWARD_OFFSET


# TODO: Use IntEnum instead?
class LocationType(Enum):
    CHEST = "Chest"
    """Location checked by opening a chest."""
    NPC_REWARD = "NPC Reward"
    """Location checked by talking to an NPC or stepping on an item tile."""
    LAIR = "Lair"
    """Location checked by sealing a monster lair."""


def address_for_location(type: LocationType, id: int) -> int:
    if type == LocationType.LAIR:
        return BASE_ID + LAIR_ID_OFFSET + id
    if type == LocationType.NPC_REWARD:
        return BASE_ID + NPC_REWARD_OFFSET + id
    return BASE_ID + id


@dataclass(frozen=True)
class SoulBlazerLocationData():
    id: int
    """Internal location ID and index into ROM chest/lair/NPC reward table"""
    type: LocationType
    flag: RuleFlag = RuleFlag.NONE
    # TODO: What other location properties are needed?

    @property
    def address(self) -> int:
        """The unique ID used by archipelago for this location"""

        if self.type == LocationType.LAIR:
            return BASE_ID + LAIR_ID_OFFSET + self.id
        if self.type == LocationType.NPC_REWARD:
            return BASE_ID + NPC_REWARD_OFFSET + self.id
        return BASE_ID + self.id


class SoulBlazerLocation(Location):
    game = "Soul Blazer"

    def __init__(
        self, player: int, name: str, data: SoulBlazerLocationData, parent: Optional[Region] = None
    ):
        super().__init__(player, name, data.address, parent)
        self.data: SoulBlazerLocationData = data
        self.access_rule = get_rule_for_location(name, player, self.data.flag)


# TODO: move data into yaml or json
chest_table = {
    ChestName.TRIAL_ROOM                     : SoulBlazerLocationData(ChestID.TRIAL_ROOM                    , LocationType.CHEST),
    ChestName.GRASS_VALLEY_SECRET_CAVE_LEFT  : SoulBlazerLocationData(ChestID.GRASS_VALLEY_SECRET_CAVE_LEFT , LocationType.CHEST),
    ChestName.GRASS_VALLEY_SECRET_CAVE_RIGHT : SoulBlazerLocationData(ChestID.GRASS_VALLEY_SECRET_CAVE_RIGHT, LocationType.CHEST),
    ChestName.UNDERGROUND_CASTLE_12GEM       : SoulBlazerLocationData(ChestID.UNDERGROUND_CASTLE_12GEM      , LocationType.CHEST),
    ChestName.UNDERGROUND_CASTLE_HERB        : SoulBlazerLocationData(ChestID.UNDERGROUND_CASTLE_HERB       , LocationType.CHEST),
    ChestName.UNDERGROUND_CASTLE_DREAM_ROD   : SoulBlazerLocationData(ChestID.UNDERGROUND_CASTLE_DREAM_ROD  , LocationType.CHEST),
    ChestName.UNDERGROUND_CASTLE_LEOS_BRUSH  : SoulBlazerLocationData(ChestID.UNDERGROUND_CASTLE_LEOS_BRUSH , LocationType.CHEST),
    ChestName.LEOS_PAINTING_HERB             : SoulBlazerLocationData(ChestID.LEOS_PAINTING_HERB            , LocationType.CHEST),
    ChestName.LEOS_PAINTING_TORNADO          : SoulBlazerLocationData(ChestID.LEOS_PAINTING_TORNADO         , LocationType.CHEST, RuleFlag.CAN_CUT_METAL),
    ChestName.GREENWOOD_ICE_ARMOR            : SoulBlazerLocationData(ChestID.GREENWOOD_ICE_ARMOR           , LocationType.CHEST),
    ChestName.GREENWOOD_TUNNELS              : SoulBlazerLocationData(ChestID.GREENWOOD_TUNNELS             , LocationType.CHEST),
    ChestName.WATER_SHRINE_1                 : SoulBlazerLocationData(ChestID.WATER_SHRINE_1                , LocationType.CHEST),
    ChestName.WATER_SHRINE_2_N               : SoulBlazerLocationData(ChestID.WATER_SHRINE_2_N              , LocationType.CHEST),
    ChestName.WATER_SHRINE_2_HERB            : SoulBlazerLocationData(ChestID.WATER_SHRINE_2_HERB           , LocationType.CHEST),
    ChestName.WATER_SHRINE_3_SW              : SoulBlazerLocationData(ChestID.WATER_SHRINE_3_SW             , LocationType.CHEST),
    ChestName.WATER_SHRINE_3_SE              : SoulBlazerLocationData(ChestID.WATER_SHRINE_3_SE             , LocationType.CHEST),
    ChestName.FIRE_SHRINE_1                  : SoulBlazerLocationData(ChestID.FIRE_SHRINE_1                 , LocationType.CHEST),
    ChestName.FIRE_SHRINE_2_DISAPPEARING     : SoulBlazerLocationData(ChestID.FIRE_SHRINE_2_DISAPPEARING    , LocationType.CHEST),
    ChestName.FIRE_SHRINE_2_SCORPION         : SoulBlazerLocationData(ChestID.FIRE_SHRINE_2_SCORPION        , LocationType.CHEST, RuleFlag.CAN_CUT_METAL),
    ChestName.FIRE_SHRINE_3_100GEM           : SoulBlazerLocationData(ChestID.FIRE_SHRINE_3_100GEM          , LocationType.CHEST),
    ChestName.FIRE_SHRINE_3_60GEM            : SoulBlazerLocationData(ChestID.FIRE_SHRINE_3_60GEM           , LocationType.CHEST),
    ChestName.LIGHT_SHRINE                   : SoulBlazerLocationData(ChestID.LIGHT_SHRINE                  , LocationType.CHEST, RuleFlag.CAN_CUT_SPIRIT),
    ChestName.ST_ELLIS_MERMAIDS_TEARS        : SoulBlazerLocationData(ChestID.ST_ELLIS_MERMAIDS_TEARS       , LocationType.CHEST),
    ChestName.ST_ELLIS_BIG_PEARL             : SoulBlazerLocationData(ChestID.ST_ELLIS_BIG_PEARL            , LocationType.CHEST),
    ChestName.SEABED_SECRET_TL               : SoulBlazerLocationData(ChestID.SEABED_SECRET_TL              , LocationType.CHEST),
    ChestName.SEABED_SECRET_TR               : SoulBlazerLocationData(ChestID.SEABED_SECRET_TR              , LocationType.CHEST),
    ChestName.SEABED_SECRET_BL               : SoulBlazerLocationData(ChestID.SEABED_SECRET_BL              , LocationType.CHEST),
    ChestName.SEABED_SECRET_BR               : SoulBlazerLocationData(ChestID.SEABED_SECRET_BR              , LocationType.CHEST),
    ChestName.SOUTHERTA                      : SoulBlazerLocationData(ChestID.SOUTHERTA                     , LocationType.CHEST),
    ChestName.ROCKBIRD_HERB                  : SoulBlazerLocationData(ChestID.ROCKBIRD_HERB                 , LocationType.CHEST),
    ChestName.ROCKBIRD_60GEM                 : SoulBlazerLocationData(ChestID.ROCKBIRD_60GEM                , LocationType.CHEST),
    ChestName.DUREAN_CRITICAL_SWORD          : SoulBlazerLocationData(ChestID.DUREAN_CRITICAL_SWORD         , LocationType.CHEST),
    ChestName.DUREAN_STRANGE_BOTTLE          : SoulBlazerLocationData(ChestID.DUREAN_STRANGE_BOTTLE         , LocationType.CHEST),
    ChestName.GHOST_SHIP                     : SoulBlazerLocationData(ChestID.GHOST_SHIP                    , LocationType.CHEST),
    ChestName.SEABED_POWER_BRACELET          : SoulBlazerLocationData(ChestID.SEABED_POWER_BRACELET         , LocationType.CHEST),
    ChestName.MOUNTAIN_OF_SOULS_1            : SoulBlazerLocationData(ChestID.MOUNTAIN_OF_SOULS_1           , LocationType.CHEST),
    ChestName.MOUNTAIN_OF_SOULS_2_LL         : SoulBlazerLocationData(ChestID.MOUNTAIN_OF_SOULS_2_LL        , LocationType.CHEST),
    ChestName.MOUNTAIN_OF_SOULS_2_L          : SoulBlazerLocationData(ChestID.MOUNTAIN_OF_SOULS_2_L         , LocationType.CHEST),
    ChestName.MOUNTAIN_OF_SOULS_2_R          : SoulBlazerLocationData(ChestID.MOUNTAIN_OF_SOULS_2_R         , LocationType.CHEST),
    ChestName.MOUNTAIN_OF_SOULS_2_RR         : SoulBlazerLocationData(ChestID.MOUNTAIN_OF_SOULS_2_RR        , LocationType.CHEST),
    ChestName.LAYNOLE_LUCKY_BLADE            : SoulBlazerLocationData(ChestID.LAYNOLE_LUCKY_BLADE           , LocationType.CHEST),
    ChestName.LAYNOLE_HERB                   : SoulBlazerLocationData(ChestID.LAYNOLE_HERB                  , LocationType.CHEST),
    ChestName.LAYNOLE_ROTATOR                : SoulBlazerLocationData(ChestID.LAYNOLE_ROTATOR               , LocationType.CHEST),
    ChestName.LEOS_LAB_ZANTETSU              : SoulBlazerLocationData(ChestID.LEOS_LAB_ZANTETSU             , LocationType.CHEST),
    ChestName.POWER_PLANT_LIGHT_ARMOR        : SoulBlazerLocationData(ChestID.POWER_PLANT_LIGHT_ARMOR       , LocationType.CHEST, RuleFlag.CAN_CUT_METAL),
    ChestName.MODEL_TOWN_1_SE                : SoulBlazerLocationData(ChestID.MODEL_TOWN_1_SE               , LocationType.CHEST),
    ChestName.MODEL_TOWN_1_NL                : SoulBlazerLocationData(ChestID.MODEL_TOWN_1_NL               , LocationType.CHEST),
    ChestName.MODEL_TOWN_1_NR                : SoulBlazerLocationData(ChestID.MODEL_TOWN_1_NR               , LocationType.CHEST),
    ChestName.MODEL_TOWN_2_TOP               : SoulBlazerLocationData(ChestID.MODEL_TOWN_2_TOP              , LocationType.CHEST),
    ChestName.MODEL_TOWN_2_BOT               : SoulBlazerLocationData(ChestID.MODEL_TOWN_2_BOT              , LocationType.CHEST),
    ChestName.CASTLE_BASEMENT_1_W            : SoulBlazerLocationData(ChestID.CASTLE_BASEMENT_1_W           , LocationType.CHEST),
    ChestName.CASTLE_BASEMENT_1_SPIRIT_SWORD : SoulBlazerLocationData(ChestID.CASTLE_BASEMENT_1_SPIRIT_SWORD, LocationType.CHEST),
    ChestName.CASTLE_BASEMENT_2_N            : SoulBlazerLocationData(ChestID.CASTLE_BASEMENT_2_N           , LocationType.CHEST),
    ChestName.CASTLE_BASEMENT_2_SW           : SoulBlazerLocationData(ChestID.CASTLE_BASEMENT_2_SW          , LocationType.CHEST),
    ChestName.CASTLE_BASEMENT_2_MIDDLE       : SoulBlazerLocationData(ChestID.CASTLE_BASEMENT_2_MIDDLE      , LocationType.CHEST),
    ChestName.CASTLE_BASEMENT_3              : SoulBlazerLocationData(ChestID.CASTLE_BASEMENT_3             , LocationType.CHEST),
    ChestName.CASTLE_RIGHT_TOWER_2_L         : SoulBlazerLocationData(ChestID.CASTLE_RIGHT_TOWER_2_L        , LocationType.CHEST),
    ChestName.CASTLE_RIGHT_TOWER_2_R         : SoulBlazerLocationData(ChestID.CASTLE_RIGHT_TOWER_2_R        , LocationType.CHEST),
    ChestName.CASTLE_RIGHT_TOWER_3_TL        : SoulBlazerLocationData(ChestID.CASTLE_RIGHT_TOWER_3_TL       , LocationType.CHEST),
    ChestName.CASTLE_RIGHT_TOWER_3_BR        : SoulBlazerLocationData(ChestID.CASTLE_RIGHT_TOWER_3_BR       , LocationType.CHEST),
    ChestName.WOE_1_SE                       : SoulBlazerLocationData(ChestID.WOE_1_SE                      , LocationType.CHEST, RuleFlag.HAS_MAGIC),
    ChestName.WOE_1_SW                       : SoulBlazerLocationData(ChestID.WOE_1_SW                      , LocationType.CHEST, RuleFlag.HAS_MAGIC),
    ChestName.WOE_1_REDHOT_BALL              : SoulBlazerLocationData(ChestID.WOE_1_REDHOT_BALL             , LocationType.CHEST, RuleFlag.HAS_MAGIC),
    ChestName.WOE_2                          : SoulBlazerLocationData(ChestID.WOE_2                         , LocationType.CHEST),
    ChestName.DAZZLING_SPACE_SE              : SoulBlazerLocationData(ChestID.DAZZLING_SPACE_SE             , LocationType.CHEST),
    ChestName.DAZZLING_SPACE_SW              : SoulBlazerLocationData(ChestID.DAZZLING_SPACE_SW             , LocationType.CHEST),
}

npc_reward_table = {
    NPCRewardName.TOOL_SHOP_OWNER                  : SoulBlazerLocationData(NPCRewardID.TOOL_SHOP_OWNER                 , LocationType.NPC_REWARD),
    NPCRewardName.EMBLEM_A_TILE                    : SoulBlazerLocationData(NPCRewardID.EMBLEM_A_TILE                   , LocationType.NPC_REWARD),
    NPCRewardName.GOAT_PEN_CORNER                  : SoulBlazerLocationData(NPCRewardID.GOAT_PEN_CORNER                 , LocationType.NPC_REWARD),
    NPCRewardName.TEDDY                            : SoulBlazerLocationData(NPCRewardID.TEDDY                           , LocationType.NPC_REWARD),
    NPCRewardName.PASS_TILE                        : SoulBlazerLocationData(NPCRewardID.PASS_TILE                       , LocationType.NPC_REWARD),
    NPCRewardName.TILE_IN_CHILDS_SECRET_CAVE       : SoulBlazerLocationData(NPCRewardID.TILE_IN_CHILDS_SECRET_CAVE      , LocationType.NPC_REWARD),
    NPCRewardName.VILLAGE_CHIEF                    : SoulBlazerLocationData(NPCRewardID.VILLAGE_CHIEF                   , LocationType.NPC_REWARD),
    NPCRewardName.MAGICIAN                         : SoulBlazerLocationData(NPCRewardID.MAGICIAN                        , LocationType.NPC_REWARD, RuleFlag.HAS_SWORD),
    NPCRewardName.RECOVERY_SWORD_CRYSTAL           : SoulBlazerLocationData(NPCRewardID.RECOVERY_SWORD_CRYSTAL          , LocationType.NPC_REWARD),
    NPCRewardName.GRASS_VALLEY_SECRET_ROOM_CRYSTAL : SoulBlazerLocationData(NPCRewardID.GRASS_VALLEY_SECRET_ROOM_CRYSTAL, LocationType.NPC_REWARD),
    NPCRewardName.UNDERGROUND_CASTLE_CRYSTAL       : SoulBlazerLocationData(NPCRewardID.UNDERGROUND_CASTLE_CRYSTAL      , LocationType.NPC_REWARD),
    NPCRewardName.REDHOT_MIRROR_BIRD               : SoulBlazerLocationData(NPCRewardID.REDHOT_MIRROR_BIRD              , LocationType.NPC_REWARD),
    NPCRewardName.MAGIC_BELL_CRYSTAL               : SoulBlazerLocationData(NPCRewardID.MAGIC_BELL_CRYSTAL              , LocationType.NPC_REWARD),
    NPCRewardName.WOODSTIN_TRIO                    : SoulBlazerLocationData(NPCRewardID.WOODSTIN_TRIO                   , LocationType.NPC_REWARD),
    NPCRewardName.GREENWOODS_GUARDIAN              : SoulBlazerLocationData(NPCRewardID.GREENWOODS_GUARDIAN             , LocationType.NPC_REWARD),
    NPCRewardName.GREENWOOD_LEAVES_TILE            : SoulBlazerLocationData(NPCRewardID.GREENWOOD_LEAVES_TILE           , LocationType.NPC_REWARD),
    NPCRewardName.SHIELD_BRACELET_MOLE             : SoulBlazerLocationData(NPCRewardID.SHIELD_BRACELET_MOLE            , LocationType.NPC_REWARD),
    NPCRewardName.PSYCHO_SWORD_SQUIRREL            : SoulBlazerLocationData(NPCRewardID.PSYCHO_SWORD_SQUIRREL           , LocationType.NPC_REWARD),
    NPCRewardName.EMBLEM_C_SQUIRREL                : SoulBlazerLocationData(NPCRewardID.EMBLEM_C_SQUIRREL               , LocationType.NPC_REWARD),
    NPCRewardName.WATER_SHRINE_TILE                : SoulBlazerLocationData(NPCRewardID.WATER_SHRINE_STRANGE_BOTTLE     , LocationType.NPC_REWARD),
    NPCRewardName.LIGHT_ARROW_CRYSTAL              : SoulBlazerLocationData(NPCRewardID.LIGHT_ARROW_CRYSTAL             , LocationType.NPC_REWARD),
    NPCRewardName.LOST_MARSH_CRYSTAL               : SoulBlazerLocationData(NPCRewardID.LOST_MARSH_CRYSTAL              , LocationType.NPC_REWARD),
    NPCRewardName.WATER_SHRINE_CRYSTAL             : SoulBlazerLocationData(NPCRewardID.WATER_SHRINE_CRYSTAL            , LocationType.NPC_REWARD),
    NPCRewardName.FIRE_SHRINE_CRYSTAL              : SoulBlazerLocationData(NPCRewardID.FIRE_SHRINE_CRYSTAL             , LocationType.NPC_REWARD, RuleFlag.CAN_CUT_METAL),
    NPCRewardName.MOUNTAIN_KING                    : SoulBlazerLocationData(NPCRewardID.MOUNTAIN_KING                   , LocationType.NPC_REWARD),
    NPCRewardName.MUSHROOM_SHOES_BOY               : SoulBlazerLocationData(NPCRewardID.MUSHROOM_SHOES_BOY              , LocationType.NPC_REWARD),
    NPCRewardName.NOME                             : SoulBlazerLocationData(NPCRewardID.NOME                            , LocationType.NPC_REWARD),
    NPCRewardName.EMBLEM_E_SNAIL                   : SoulBlazerLocationData(NPCRewardID.EMBLEM_E_SNAIL                  , LocationType.NPC_REWARD),
    NPCRewardName.EMBLEM_F_TILE                    : SoulBlazerLocationData(NPCRewardID.EMBLEM_F_TILE                   , LocationType.NPC_REWARD),
    NPCRewardName.MOUNTAIN_OF_SOULS_CRYSTAL        : SoulBlazerLocationData(NPCRewardID.MOUNTAIN_OF_SOULS_CRYSTAL       , LocationType.NPC_REWARD),
    NPCRewardName.LUNE_CRYSTAL                     : SoulBlazerLocationData(NPCRewardID.LUNE_CRYSTAL                    , LocationType.NPC_REWARD),
    NPCRewardName.EMBLEM_G_UNDER_CHEST_OF_DRAWERS  : SoulBlazerLocationData(NPCRewardID.EMBLEM_G_UNDER_CHEST_OF_DRAWERS , LocationType.NPC_REWARD),
    NPCRewardName.CHEST_OF_DRAWERS_MYSTIC_ARMOR    : SoulBlazerLocationData(NPCRewardID.CHEST_OF_DRAWERS_MYSTIC_ARMOR   , LocationType.NPC_REWARD),
    NPCRewardName.HERB_PLANT_IN_LEOS_LAB           : SoulBlazerLocationData(NPCRewardID.HERB_PLANT_IN_LEOS_LAB          , LocationType.NPC_REWARD),
    NPCRewardName.LEOS_CAT_DOOR_KEY                : SoulBlazerLocationData(NPCRewardID.LEOS_CAT_DOOR_KEY               , LocationType.NPC_REWARD),
    NPCRewardName.ACTINIDIA_PLANT                  : SoulBlazerLocationData(NPCRewardID.ACTINIDIA_PLANT                 , LocationType.NPC_REWARD),
    NPCRewardName.CHEST_OF_DRAWERS_HERB            : SoulBlazerLocationData(NPCRewardID.CHEST_OF_DRAWERS_HERB           , LocationType.NPC_REWARD),
    NPCRewardName.MARIE                            : SoulBlazerLocationData(NPCRewardID.MARIE                           , LocationType.NPC_REWARD),
    NPCRewardName.SPARK_BOMB_MOUSE                 : SoulBlazerLocationData(NPCRewardID.SPARK_BOMB_MOUSE                , LocationType.NPC_REWARD),
    NPCRewardName.LEOS_LAB_BASEMENT_CRYSTAL        : SoulBlazerLocationData(NPCRewardID.LEOS_LAB_BASEMENT_CRYSTAL       , LocationType.NPC_REWARD),
    NPCRewardName.MODEL_TOWN_1_CRYSTAL             : SoulBlazerLocationData(NPCRewardID.MODEL_TOWN_1_CRYSTAL            , LocationType.NPC_REWARD),
    NPCRewardName.POWER_PLANT_CRYSTAL              : SoulBlazerLocationData(NPCRewardID.POWER_PLANT_CRYSTAL             , LocationType.NPC_REWARD, RuleFlag.CAN_CUT_METAL),
    NPCRewardName.ELEMENTAL_MAIL_SOLDIER           : SoulBlazerLocationData(NPCRewardID.ELEMENTAL_MAIL_SOLDIER          , LocationType.NPC_REWARD),
    NPCRewardName.SUPER_BRACELET_TILE              : SoulBlazerLocationData(NPCRewardID.SUPER_BRACELET_TILE             , LocationType.NPC_REWARD),
    NPCRewardName.QUEEN_MAGRIDD_VIP_CARD           : SoulBlazerLocationData(NPCRewardID.QUEEN_MAGRIDD_VIP_CARD          , LocationType.NPC_REWARD),
    NPCRewardName.PLATINUM_CARD_SOLDIER            : SoulBlazerLocationData(NPCRewardID.PLATINUM_CARD_SOLDIER           , LocationType.NPC_REWARD),
    NPCRewardName.MAID_HERB                        : SoulBlazerLocationData(NPCRewardID.MAID_HERB                       , LocationType.NPC_REWARD),
    NPCRewardName.EMBLEM_H_TILE                    : SoulBlazerLocationData(NPCRewardID.EMBLEM_H_TILE                   , LocationType.NPC_REWARD),
    NPCRewardName.KING_MAGRIDD                     : SoulBlazerLocationData(NPCRewardID.KING_MAGRIDD                    , LocationType.NPC_REWARD),
    NPCRewardName.LEO_ON_THE_AIRSHIP_DECK          : SoulBlazerLocationData(NPCRewardID.LEO_ON_THE_AIRSHIP_DECK         , LocationType.NPC_REWARD),
    NPCRewardName.HARP_STRING_TILE                 : SoulBlazerLocationData(NPCRewardID.HARP_STRING_TILE                , LocationType.NPC_REWARD),
    NPCRewardName.NORTHEASTERN_MERMAID_HERB        : SoulBlazerLocationData(NPCRewardID.NORTHEASTERN_MERMAID_HERB       , LocationType.NPC_REWARD),
    NPCRewardName.BUBBLE_ARMOR_MERMAID             : SoulBlazerLocationData(NPCRewardID.BUBBLE_ARMOR_MERMAID            , LocationType.NPC_REWARD),
    NPCRewardName.MAGIC_FLARE_MERMAID              : SoulBlazerLocationData(NPCRewardID.MAGIC_FLARE_MERMAID             , LocationType.NPC_REWARD),
    NPCRewardName.MERMAID_QUEEN                    : SoulBlazerLocationData(NPCRewardID.MERMAID_QUEEN                   , LocationType.NPC_REWARD),
    NPCRewardName.REDHOT_STICK_MERMAID             : SoulBlazerLocationData(NPCRewardID.REDHOT_STICK_MERMAID            , LocationType.NPC_REWARD),
    NPCRewardName.LUE                              : SoulBlazerLocationData(NPCRewardID.LUE                             , LocationType.NPC_REWARD),
    NPCRewardName.ROCKBIRD_CRYSTAL                 : SoulBlazerLocationData(NPCRewardID.ROCKBIRD_CRYSTAL                , LocationType.NPC_REWARD),
    NPCRewardName.SEABED_CRYSTAL_NEAR_BLESTER      : SoulBlazerLocationData(NPCRewardID.SEABED_CRYSTAL_NEAR_BLESTER     , LocationType.NPC_REWARD),
    NPCRewardName.SEABED_CRYSTAL_NEAR_DUREAN       : SoulBlazerLocationData(NPCRewardID.SEABED_CRYSTAL_NEAR_DUREAN      , LocationType.NPC_REWARD),

    NPCRewardName.MAGICIAN_SOUL                    : SoulBlazerLocationData(NPCRewardID.MAGICIAN_SOUL                   , LocationType.NPC_REWARD, RuleFlag.HAS_SWORD),
    NPCRewardName.MOLE_SOUL_OF_LIGHT               : SoulBlazerLocationData(NPCRewardID.MOLE_SOUL_OF_LIGHT              , LocationType.NPC_REWARD),
    NPCRewardName.ANGELFISH_SOUL_OF_SHIELD         : SoulBlazerLocationData(NPCRewardID.ANGELFISH_SOUL_OF_SHIELD        , LocationType.NPC_REWARD),
    NPCRewardName.GREAT_DOOR_SOUL_OF_DETECTION     : SoulBlazerLocationData(NPCRewardID.GREAT_DOOR_SOUL_OF_DETECTION    , LocationType.NPC_REWARD),
    NPCRewardName.SOLDIER_SOUL_OF_REALITY          : SoulBlazerLocationData(NPCRewardID.SOLDIER_SOUL_OF_REALITY         , LocationType.NPC_REWARD),
}

lair_table = {
    LairName.OLD_WOMAN                     : SoulBlazerLocationData(LairID.OLD_WOMAN                    , LocationType.LAIR),
    LairName.TOOL_SHOP_OWNER               : SoulBlazerLocationData(LairID.TOOL_SHOP_OWNER              , LocationType.LAIR),
    LairName.TULIP                         : SoulBlazerLocationData(LairID.TULIP                        , LocationType.LAIR),
    LairName.BRIDGE_GUARD                  : SoulBlazerLocationData(LairID.BRIDGE_GUARD                 , LocationType.LAIR),
    LairName.VILLAGE_CHIEF                 : SoulBlazerLocationData(LairID.VILLAGE_CHIEF                , LocationType.LAIR),
    LairName.IVY_CHEST_ROOM                : SoulBlazerLocationData(LairID.IVY_CHEST_ROOM               , LocationType.LAIR),
    LairName.WATER_MILL                    : SoulBlazerLocationData(LairID.WATER_MILL                   , LocationType.LAIR),
    LairName.GOAT_HERB                     : SoulBlazerLocationData(LairID.GOAT_HERB                    , LocationType.LAIR),
    LairName.LISA                          : SoulBlazerLocationData(LairID.LISA                         , LocationType.LAIR),
    LairName.TULIP2                        : SoulBlazerLocationData(LairID.TULIP2                       , LocationType.LAIR),
    LairName.ARCHITECT                     : SoulBlazerLocationData(LairID.ARCHITECT                    , LocationType.LAIR),
    LairName.IVY                           : SoulBlazerLocationData(LairID.IVY                          , LocationType.LAIR),
    LairName.GOAT                          : SoulBlazerLocationData(LairID.GOAT                         , LocationType.LAIR),
    LairName.TEDDY                         : SoulBlazerLocationData(LairID.TEDDY                        , LocationType.LAIR),
    LairName.TULIP3                        : SoulBlazerLocationData(LairID.TULIP3                       , LocationType.LAIR),
    LairName.LEOS_HOUSE                    : SoulBlazerLocationData(LairID.LEOS_HOUSE                   , LocationType.LAIR),
    LairName.LONELY_GOAT                   : SoulBlazerLocationData(LairID.LONELY_GOAT                  , LocationType.LAIR),
    LairName.TULIP_PASS                    : SoulBlazerLocationData(LairID.TULIP_PASS                   , LocationType.LAIR),
    LairName.BOY_CABIN                     : SoulBlazerLocationData(LairID.BOY_CABIN                    , LocationType.LAIR),
    LairName.BOY_CAVE                      : SoulBlazerLocationData(LairID.BOY_CAVE                     , LocationType.LAIR),
    LairName.OLD_MAN                       : SoulBlazerLocationData(LairID.OLD_MAN                      , LocationType.LAIR),
    LairName.OLD_MAN2                      : SoulBlazerLocationData(LairID.OLD_MAN2                     , LocationType.LAIR),
    LairName.IVY2                          : SoulBlazerLocationData(LairID.IVY2                         , LocationType.LAIR),
    LairName.IVY_EMBLEM_A                  : SoulBlazerLocationData(LairID.IVY_EMBLEM_A                 , LocationType.LAIR, RuleFlag.CAN_CUT_METAL),
    LairName.IVY_RECOVERY_SWORD            : SoulBlazerLocationData(LairID.IVY_RECOVERY_SWORD           , LocationType.LAIR, RuleFlag.CAN_CUT_METAL),
    LairName.TULIP4                        : SoulBlazerLocationData(LairID.TULIP4                       , LocationType.LAIR),
    LairName.GOAT2                         : SoulBlazerLocationData(LairID.GOAT2                        , LocationType.LAIR),
    LairName.BIRD_RED_HOT_MIRROR           : SoulBlazerLocationData(LairID.BIRD_RED_HOT_MIRROR          , LocationType.LAIR, RuleFlag.CAN_CUT_SPIRIT),
    LairName.BIRD                          : SoulBlazerLocationData(LairID.BIRD                         , LocationType.LAIR),
    LairName.DOG                           : SoulBlazerLocationData(LairID.DOG                          , LocationType.LAIR),
    LairName.DOG2                          : SoulBlazerLocationData(LairID.DOG2                         , LocationType.LAIR),
    LairName.DOG3                          : SoulBlazerLocationData(LairID.DOG3                         , LocationType.LAIR),
    LairName.MOLE_SHIELD_BRACELET          : SoulBlazerLocationData(LairID.MOLE_SHIELD_BRACELET         , LocationType.LAIR),
    LairName.SQUIRREL_EMBLEM_C             : SoulBlazerLocationData(LairID.SQUIRREL_EMBLEM_C            , LocationType.LAIR),
    LairName.SQUIRREL_PSYCHO_SWORD         : SoulBlazerLocationData(LairID.SQUIRREL_PSYCHO_SWORD        , LocationType.LAIR),
    LairName.BIRD2                         : SoulBlazerLocationData(LairID.BIRD2                        , LocationType.LAIR),
    LairName.MOLE_SOUL_OF_LIGHT            : SoulBlazerLocationData(LairID.MOLE_SOUL_OF_LIGHT           , LocationType.LAIR),
    LairName.DEER                          : SoulBlazerLocationData(LairID.DEER                         , LocationType.LAIR),
    LairName.CROCODILE                     : SoulBlazerLocationData(LairID.CROCODILE                    , LocationType.LAIR),
    LairName.SQUIRREL                      : SoulBlazerLocationData(LairID.SQUIRREL                     , LocationType.LAIR),
    LairName.GREENWOODS_GUARDIAN           : SoulBlazerLocationData(LairID.GREENWOODS_GUARDIAN          , LocationType.LAIR),
    LairName.MOLE                          : SoulBlazerLocationData(LairID.MOLE                         , LocationType.LAIR),
    LairName.DOG4                          : SoulBlazerLocationData(LairID.DOG4                         , LocationType.LAIR),
    LairName.SQUIRREL_ICE_ARMOR            : SoulBlazerLocationData(LairID.SQUIRREL_ICE_ARMOR           , LocationType.LAIR),
    LairName.SQUIRREL2                     : SoulBlazerLocationData(LairID.SQUIRREL2                    , LocationType.LAIR),
    LairName.DOG5                          : SoulBlazerLocationData(LairID.DOG5                         , LocationType.LAIR),
    LairName.CROCODILE2                    : SoulBlazerLocationData(LairID.CROCODILE2                   , LocationType.LAIR),
    LairName.MOLE2                         : SoulBlazerLocationData(LairID.MOLE2                        , LocationType.LAIR),
    LairName.SQUIRREL3                     : SoulBlazerLocationData(LairID.SQUIRREL3                    , LocationType.LAIR),
    LairName.BIRD_GREENWOOD_LEAF           : SoulBlazerLocationData(LairID.BIRD_GREENWOOD_LEAF          , LocationType.LAIR),
    LairName.MOLE3                         : SoulBlazerLocationData(LairID.MOLE3                        , LocationType.LAIR),
    LairName.DEER_MAGIC_BELL               : SoulBlazerLocationData(LairID.DEER_MAGIC_BELL              , LocationType.LAIR),
    LairName.BIRD3                         : SoulBlazerLocationData(LairID.BIRD3                        , LocationType.LAIR, RuleFlag.CAN_CUT_METAL),
    LairName.CROCODILE3                    : SoulBlazerLocationData(LairID.CROCODILE3                   , LocationType.LAIR),
    LairName.MONMO                         : SoulBlazerLocationData(LairID.MONMO                        , LocationType.LAIR),
    LairName.DOLPHIN                       : SoulBlazerLocationData(LairID.DOLPHIN                      , LocationType.LAIR),
    LairName.ANGELFISH                     : SoulBlazerLocationData(LairID.ANGELFISH                    , LocationType.LAIR),
    LairName.MERMAID                       : SoulBlazerLocationData(LairID.MERMAID                      , LocationType.LAIR),
    LairName.ANGELFISH2                    : SoulBlazerLocationData(LairID.ANGELFISH2                   , LocationType.LAIR),
    LairName.MERMAID_PEARL                 : SoulBlazerLocationData(LairID.MERMAID_PEARL                , LocationType.LAIR),
    LairName.MERMAID2                      : SoulBlazerLocationData(LairID.MERMAID2                     , LocationType.LAIR),
    LairName.DOLPHIN_SAVES_LUE             : SoulBlazerLocationData(LairID.DOLPHIN_SAVES_LUE            , LocationType.LAIR),
    LairName.MERMAID_STATUE_BLESTER        : SoulBlazerLocationData(LairID.MERMAID_STATUE_BLESTER       , LocationType.LAIR),
    LairName.MERMAID_RED_HOT_STICK         : SoulBlazerLocationData(LairID.MERMAID_RED_HOT_STICK        , LocationType.LAIR, RuleFlag.CAN_CUT_METAL),
    LairName.LUE                           : SoulBlazerLocationData(LairID.LUE                          , LocationType.LAIR),
    LairName.MERMAID3                      : SoulBlazerLocationData(LairID.MERMAID3                     , LocationType.LAIR),
    LairName.MERMAID_NANA                  : SoulBlazerLocationData(LairID.MERMAID_NANA                 , LocationType.LAIR),
    LairName.MERMAID4                      : SoulBlazerLocationData(LairID.MERMAID4                     , LocationType.LAIR),
    LairName.DOLPHIN2                      : SoulBlazerLocationData(LairID.DOLPHIN2                     , LocationType.LAIR),
    LairName.MERMAID_STATUE_ROCKBIRD       : SoulBlazerLocationData(LairID.MERMAID_STATUE_ROCKBIRD      , LocationType.LAIR),
    LairName.MERMAID_BUBBLE_ARMOR          : SoulBlazerLocationData(LairID.MERMAID_BUBBLE_ARMOR         , LocationType.LAIR),
    LairName.MERMAID5                      : SoulBlazerLocationData(LairID.MERMAID5                     , LocationType.LAIR),
    LairName.MERMAID6                      : SoulBlazerLocationData(LairID.MERMAID6                     , LocationType.LAIR),
    LairName.MERMAID_TEARS                 : SoulBlazerLocationData(LairID.MERMAID_TEARS                , LocationType.LAIR),
    LairName.MERMAID_STATUE_DUREAN         : SoulBlazerLocationData(LairID.MERMAID_STATUE_DUREAN        , LocationType.LAIR),
    LairName.ANGELFISH3                    : SoulBlazerLocationData(LairID.ANGELFISH3                   , LocationType.LAIR),
    LairName.ANGELFISH_SOUL_OF_SHIELD      : SoulBlazerLocationData(LairID.ANGELFISH_SOUL_OF_SHIELD     , LocationType.LAIR),
    LairName.MERMAID_MAGIC_FLARE           : SoulBlazerLocationData(LairID.MERMAID_MAGIC_FLARE          , LocationType.LAIR),
    LairName.MERMAID_QUEEN                 : SoulBlazerLocationData(LairID.MERMAID_QUEEN                , LocationType.LAIR),
    LairName.MERMAID_STATUE_GHOST_SHIP     : SoulBlazerLocationData(LairID.MERMAID_STATUE_GHOST_SHIP    , LocationType.LAIR, RuleFlag.HAS_THUNDER),
    LairName.DOLPHIN_SECRET_CAVE           : SoulBlazerLocationData(LairID.DOLPHIN_SECRET_CAVE          , LocationType.LAIR),
    LairName.MERMAID7                      : SoulBlazerLocationData(LairID.MERMAID7                     , LocationType.LAIR),
    LairName.ANGELFISH4                    : SoulBlazerLocationData(LairID.ANGELFISH4                   , LocationType.LAIR),
    LairName.MERMAID8                      : SoulBlazerLocationData(LairID.MERMAID8                     , LocationType.LAIR),
    LairName.DOLPHIN_PEARL                 : SoulBlazerLocationData(LairID.DOLPHIN_PEARL                , LocationType.LAIR),
    LairName.MERMAID9                      : SoulBlazerLocationData(LairID.MERMAID9                     , LocationType.LAIR),
    LairName.GRANDPA                       : SoulBlazerLocationData(LairID.GRANDPA                      , LocationType.LAIR),
    LairName.GIRL                          : SoulBlazerLocationData(LairID.GIRL                         , LocationType.LAIR),
    LairName.MUSHROOM                      : SoulBlazerLocationData(LairID.MUSHROOM                     , LocationType.LAIR),
    LairName.BOY                           : SoulBlazerLocationData(LairID.BOY                          , LocationType.LAIR),
    LairName.GRANDPA2                      : SoulBlazerLocationData(LairID.GRANDPA2                     , LocationType.LAIR),
    LairName.SNAIL_JOCKEY                  : SoulBlazerLocationData(LairID.SNAIL_JOCKEY                 , LocationType.LAIR),
    LairName.NOME                          : SoulBlazerLocationData(LairID.NOME                         , LocationType.LAIR),
    LairName.BOY2                          : SoulBlazerLocationData(LairID.BOY2                         , LocationType.LAIR),
    LairName.MUSHROOM_EMBLEM_F             : SoulBlazerLocationData(LairID.MUSHROOM_EMBLEM_F            , LocationType.LAIR),
    LairName.DANCING_GRANDMA               : SoulBlazerLocationData(LairID.DANCING_GRANDMA              , LocationType.LAIR),
    LairName.DANCING_GRANDMA2              : SoulBlazerLocationData(LairID.DANCING_GRANDMA2             , LocationType.LAIR),
    LairName.SNAIL_EMBLEM_E                : SoulBlazerLocationData(LairID.SNAIL_EMBLEM_E               , LocationType.LAIR),
    LairName.BOY_MUSHROOM_SHOES            : SoulBlazerLocationData(LairID.BOY_MUSHROOM_SHOES           , LocationType.LAIR),
    LairName.GRANDMA                       : SoulBlazerLocationData(LairID.GRANDMA                      , LocationType.LAIR),
    LairName.GIRL2                         : SoulBlazerLocationData(LairID.GIRL2                        , LocationType.LAIR),
    LairName.MUSHROOM2                     : SoulBlazerLocationData(LairID.MUSHROOM2                    , LocationType.LAIR),
    LairName.SNAIL_RACER                   : SoulBlazerLocationData(LairID.SNAIL_RACER                  , LocationType.LAIR),
    LairName.SNAIL_RACER2                  : SoulBlazerLocationData(LairID.SNAIL_RACER2                 , LocationType.LAIR),
    LairName.GIRL3                         : SoulBlazerLocationData(LairID.GIRL3                        , LocationType.LAIR),
    LairName.MUSHROOM3                     : SoulBlazerLocationData(LairID.MUSHROOM3                    , LocationType.LAIR),
    LairName.SNAIL                         : SoulBlazerLocationData(LairID.SNAIL                        , LocationType.LAIR),
    LairName.GRANDPA3                      : SoulBlazerLocationData(LairID.GRANDPA3                     , LocationType.LAIR),
    LairName.SNAIL2                        : SoulBlazerLocationData(LairID.SNAIL2                       , LocationType.LAIR),
    LairName.GRANDPA4                      : SoulBlazerLocationData(LairID.GRANDPA4                     , LocationType.LAIR),
    LairName.GRANDPA_LUNE                  : SoulBlazerLocationData(LairID.GRANDPA_LUNE                 , LocationType.LAIR),
    LairName.GRANDPA5                      : SoulBlazerLocationData(LairID.GRANDPA5                     , LocationType.LAIR),
    LairName.MOUNTAIN_KING                 : SoulBlazerLocationData(LairID.MOUNTAIN_KING                , LocationType.LAIR),
    LairName.PLANT_HERB                    : SoulBlazerLocationData(LairID.PLANT_HERB                   , LocationType.LAIR, RuleFlag.CAN_CUT_METAL),
    LairName.PLANT                         : SoulBlazerLocationData(LairID.PLANT                        , LocationType.LAIR),
    LairName.CHEST_OF_DRAWERS_MYSTIC_ARMOR : SoulBlazerLocationData(LairID.CHEST_OF_DRAWERS_MYSTIC_ARMOR, LocationType.LAIR, RuleFlag.CAN_CUT_METAL),
    LairName.CAT                           : SoulBlazerLocationData(LairID.CAT                          , LocationType.LAIR),
    LairName.GREAT_DOOR_ZANTETSU_SWORD     : SoulBlazerLocationData(LairID.GREAT_DOOR_ZANTETSU_SWORD    , LocationType.LAIR),
    LairName.CAT2                          : SoulBlazerLocationData(LairID.CAT2                         , LocationType.LAIR, RuleFlag.CAN_CUT_METAL),
    LairName.GREAT_DOOR                    : SoulBlazerLocationData(LairID.GREAT_DOOR                   , LocationType.LAIR, RuleFlag.CAN_CUT_METAL),
    LairName.CAT3                          : SoulBlazerLocationData(LairID.CAT3                         , LocationType.LAIR),
    LairName.MODEL_TOWN1                   : SoulBlazerLocationData(LairID.MODEL_TOWN1                  , LocationType.LAIR),
    LairName.GREAT_DOOR_MODEL_TOWNS        : SoulBlazerLocationData(LairID.GREAT_DOOR_MODEL_TOWNS       , LocationType.LAIR, RuleFlag.CAN_CUT_METAL),
    LairName.STEPS_UPSTAIRS                : SoulBlazerLocationData(LairID.STEPS_UPSTAIRS               , LocationType.LAIR, RuleFlag.CAN_CUT_METAL),
    LairName.CAT_DOOR_KEY                  : SoulBlazerLocationData(LairID.CAT_DOOR_KEY                 , LocationType.LAIR),
    LairName.MOUSE                         : SoulBlazerLocationData(LairID.MOUSE                        , LocationType.LAIR, RuleFlag.CAN_CUT_METAL),
    LairName.MARIE                         : SoulBlazerLocationData(LairID.MARIE                        , LocationType.LAIR, RuleFlag.CAN_CUT_METAL),
    LairName.DOLL                          : SoulBlazerLocationData(LairID.DOLL                         , LocationType.LAIR, RuleFlag.CAN_CUT_METAL),
    LairName.CHEST_OF_DRAWERS              : SoulBlazerLocationData(LairID.CHEST_OF_DRAWERS             , LocationType.LAIR),
    LairName.PLANT2                        : SoulBlazerLocationData(LairID.PLANT2                       , LocationType.LAIR),
    LairName.MOUSE2                        : SoulBlazerLocationData(LairID.MOUSE2                       , LocationType.LAIR),
    LairName.MOUSE_SPARK_BOMB              : SoulBlazerLocationData(LairID.MOUSE_SPARK_BOMB             , LocationType.LAIR, RuleFlag.HAS_MAGIC),
    LairName.MOUSE3                        : SoulBlazerLocationData(LairID.MOUSE3                       , LocationType.LAIR, RuleFlag.HAS_MAGIC),
    LairName.GREAT_DOOR_SOUL_OF_DETECTION  : SoulBlazerLocationData(LairID.GREAT_DOOR_SOUL_OF_DETECTION , LocationType.LAIR),
    LairName.MODEL_TOWN2                   : SoulBlazerLocationData(LairID.MODEL_TOWN2                  , LocationType.LAIR, RuleFlag.HAS_MAGIC),
    LairName.MOUSE4                        : SoulBlazerLocationData(LairID.MOUSE4                       , LocationType.LAIR, RuleFlag.HAS_MAGIC),
    LairName.STEPS_MARIE                   : SoulBlazerLocationData(LairID.STEPS_MARIE                  , LocationType.LAIR, RuleFlag.HAS_MAGIC),
    LairName.CHEST_OF_DRAWERS2             : SoulBlazerLocationData(LairID.CHEST_OF_DRAWERS2            , LocationType.LAIR),
    LairName.PLANT_ACTINIDIA_LEAVES        : SoulBlazerLocationData(LairID.PLANT_ACTINIDIA_LEAVES       , LocationType.LAIR),
    LairName.MOUSE5                        : SoulBlazerLocationData(LairID.MOUSE5                       , LocationType.LAIR),
    LairName.CAT4                          : SoulBlazerLocationData(LairID.CAT4                         , LocationType.LAIR),
    LairName.STAIRS_POWER_PLANT            : SoulBlazerLocationData(LairID.STAIRS_POWER_PLANT           , LocationType.LAIR),
    LairName.SOLDIER                       : SoulBlazerLocationData(LairID.SOLDIER                      , LocationType.LAIR),
    LairName.SOLDIER2                      : SoulBlazerLocationData(LairID.SOLDIER2                     , LocationType.LAIR, RuleFlag.CAN_CUT_SPIRIT),
    LairName.SOLDIER3                      : SoulBlazerLocationData(LairID.SOLDIER3                     , LocationType.LAIR, RuleFlag.CAN_CUT_SPIRIT),
    LairName.SOLDIER_ELEMENTAL_MAIL        : SoulBlazerLocationData(LairID.SOLDIER_ELEMENTAL_MAIL       , LocationType.LAIR, RuleFlag.CAN_CUT_SPIRIT),
    LairName.SOLDIER4                      : SoulBlazerLocationData(LairID.SOLDIER4                     , LocationType.LAIR, RuleFlag.CAN_CUT_SPIRIT),
    LairName.SOLDIER5                      : SoulBlazerLocationData(LairID.SOLDIER5                     , LocationType.LAIR),
    LairName.SINGER_CONCERT_HALL           : SoulBlazerLocationData(LairID.SINGER_CONCERT_HALL          , LocationType.LAIR, RuleFlag.CAN_CUT_SPIRIT),
    LairName.SOLDIER6                      : SoulBlazerLocationData(LairID.SOLDIER6                     , LocationType.LAIR),
    LairName.MAID                          : SoulBlazerLocationData(LairID.MAID                         , LocationType.LAIR, RuleFlag.CAN_CUT_SPIRIT),
    LairName.SOLDIER_LEFT_TOWER            : SoulBlazerLocationData(LairID.SOLDIER_LEFT_TOWER           , LocationType.LAIR),
    LairName.SOLDIER_DOK                   : SoulBlazerLocationData(LairID.SOLDIER_DOK                  , LocationType.LAIR),
    LairName.SOLDIER_PLATINUM_CARD         : SoulBlazerLocationData(LairID.SOLDIER_PLATINUM_CARD        , LocationType.LAIR, RuleFlag.CAN_CUT_SPIRIT),
    LairName.SINGER                        : SoulBlazerLocationData(LairID.SINGER                       , LocationType.LAIR, RuleFlag.CAN_CUT_SPIRIT),
    LairName.SOLDIER_SOUL_OF_REALITY       : SoulBlazerLocationData(LairID.SOLDIER_SOUL_OF_REALITY      , LocationType.LAIR),
    LairName.MAID2                         : SoulBlazerLocationData(LairID.MAID2                        , LocationType.LAIR),
    LairName.QUEEN_MAGRIDD                 : SoulBlazerLocationData(LairID.QUEEN_MAGRIDD                , LocationType.LAIR),
    LairName.SOLDIER_WITH_LEO              : SoulBlazerLocationData(LairID.SOLDIER_WITH_LEO             , LocationType.LAIR),
    LairName.SOLDIER_RIGHT_TOWER           : SoulBlazerLocationData(LairID.SOLDIER_RIGHT_TOWER          , LocationType.LAIR),
    LairName.DR_LEO                        : SoulBlazerLocationData(LairID.DR_LEO                       , LocationType.LAIR),
    LairName.SOLDIER7                      : SoulBlazerLocationData(LairID.SOLDIER7                     , LocationType.LAIR),
    LairName.SOLDIER8                      : SoulBlazerLocationData(LairID.SOLDIER8                     , LocationType.LAIR),
    LairName.MAID_HERB                     : SoulBlazerLocationData(LairID.MAID_HERB                    , LocationType.LAIR),
    LairName.SOLDIER_CASTLE                : SoulBlazerLocationData(LairID.SOLDIER_CASTLE               , LocationType.LAIR),
    LairName.SOLDIER9                      : SoulBlazerLocationData(LairID.SOLDIER9                     , LocationType.LAIR),
    LairName.SOLDIER10                     : SoulBlazerLocationData(LairID.SOLDIER10                    , LocationType.LAIR),
    LairName.SOLDIER11                     : SoulBlazerLocationData(LairID.SOLDIER11                    , LocationType.LAIR),
    LairName.KING_MAGRIDD                  : SoulBlazerLocationData(LairID.KING_MAGRIDD                 , LocationType.LAIR),
}

all_locations_table = {
    **chest_table,
    **npc_reward_table,
    **lair_table,
}

boss_lair_names_table = {
    LairName.VILLAGE_CHIEF,
    LairName.GREENWOODS_GUARDIAN,
    LairName.MERMAID_QUEEN,
    LairName.MOUNTAIN_KING,
    LairName.MARIE,
    LairName.KING_MAGRIDD,
}

village_leader_names_table = {
    NPCRewardName.VILLAGE_CHIEF,
    NPCRewardName.GREENWOODS_GUARDIAN,
    NPCRewardName.MERMAID_QUEEN,
    NPCRewardName.NOME,
    NPCRewardName.MARIE,
    NPCRewardName.KING_MAGRIDD,
}

