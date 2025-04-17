from random import Random
from .Data.Lair import lair_data, LairDataRaw
from .Data.Enums import LairAct, LairBehavior, EnemyType
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import SoulBlazerWorld

no_fish_lair_ids: set[int] = {125, 137, 141, 147, 164, 165, 169, 170, 178, 186, 187, 191, 192}
"""These lairs can't have fish enemies, or the game crashes."""

no_metal_lair_ids: set[int] = {267, 269, 270, 274, 302}
"""Lairs assumed beatable without Zantetsu Sword."""

no_ghost_lair_ids: set[int] = {345, 348, 350}
"""Lairs assumed beatable without Spirit Sword."""

must_be_metal_lair_ids: set[int] = {277, 308}
"""Lairs Logically requiring Zantetsu Sword."""

must_be_ghost_lair_ids: set[int] = {349}
"""Lairs Logically requiring Spirit Sword."""

must_not_enemize_lair_ids: set[int] = {109, 199, 202, 206, 275, 310}
"""Lairs which should not be enemized."""

must_not_be_upwards_lair_ids: set[int] = {71}
"""Lairs which cannot have enemies oriented upwards."""

underground_castle_enemies: list[EnemyType] = [
    EnemyType.ACT1_GOBLIN,
    EnemyType.ACT1_IMP,
    EnemyType.ACT1_FLY,
    EnemyType.ACT1_PLANT,
    EnemyType.ACT1_SLIME,
    EnemyType.ACT1_TORCH,
]

leos_paintings_enemies: list[EnemyType] = [
    EnemyType.ACT1_ARMOR,
    EnemyType.ACT1_BIRD,
    EnemyType.ACT1_TORCH2,
    EnemyType.ACT1_BLOCK,
]

water_shrine_enemies: list[EnemyType] = [
    EnemyType.ACT2_MUDMAN,
    EnemyType.ACT2_BUSH,
    EnemyType.ACT2_STATUE,
    EnemyType.ACT2_FLOWER,
]

fire_light_shrine_enemies: list[EnemyType] = [
    EnemyType.ACT2_FIRE_SPIRIT,
    EnemyType.ACT2_GHOST,
    EnemyType.ACT2_LIZARDMAN,
    EnemyType.ACT2_TP_LIZARDMAN,
    EnemyType.ACT2_FIREMAN,
]

fire_light_shrine_enemies_no_fire_spirit: list[EnemyType] = [
    EnemyType.ACT2_GHOST,
    EnemyType.ACT2_LIZARDMAN,
    EnemyType.ACT2_TP_LIZARDMAN,
    EnemyType.ACT2_FIREMAN,
]

seabed_enemies: list[EnemyType] = [
    EnemyType.ACT3_URCHIN,
    EnemyType.ACT3_JELLYFISH,
    EnemyType.ACT3_CRAB,
    EnemyType.ACT3_RAY,
    EnemyType.ACT3_SEAHORSE,
]

island_enemies: list[EnemyType] = [
    EnemyType.ACT3_PALM_TREE,
    EnemyType.ACT3_ROCK,
    EnemyType.ACT3_FISH,
    EnemyType.ACT3_GORILLA,
    EnemyType.ACT3_EAGLE,
]

island_enemies_no_fish: list[EnemyType] = [
    EnemyType.ACT3_PALM_TREE,
    EnemyType.ACT3_ROCK,
    EnemyType.ACT3_GORILLA,
    EnemyType.ACT3_EAGLE,
]

mountain_enemies: list[EnemyType] = [
    EnemyType.ACT4_RAT,
    EnemyType.ACT4_MOOSE,
    EnemyType.ACT4_YETI,
    EnemyType.ACT4_BAT,
    EnemyType.ACT4_SNOWBALL,
]

mountain_enemies_no_snowball: list[EnemyType] = [
    EnemyType.ACT4_RAT,
    EnemyType.ACT4_MOOSE,
    EnemyType.ACT4_YETI,
    EnemyType.ACT4_BAT,
]

laynole_lune_enemies: list[EnemyType] = [
    EnemyType.ACT4_PURPLE_WIZARD,
    EnemyType.ACT4_RED_WIZARD,
    EnemyType.ACT4_ICE_HEAD,
    EnemyType.ACT4_ICE_BLOCK,
    EnemyType.ACT4_CIRCLING_BAT,
    EnemyType.ACT4_SLIME,
]

laynole_lune_enemies_no_ice_block: list[EnemyType] = [
    EnemyType.ACT4_PURPLE_WIZARD,
    EnemyType.ACT4_RED_WIZARD,
    EnemyType.ACT4_ICE_HEAD,
    EnemyType.ACT4_CIRCLING_BAT,
    EnemyType.ACT4_SLIME,
]

leos_basement_enemies: list[EnemyType] = [
    EnemyType.ACT5_METAL_MOUSE,
    EnemyType.ACT5_BULLDOZER,
    EnemyType.ACT5_HELICOPTER,
    EnemyType.ACT5_WORM,
    EnemyType.ACT5_ROBOT,
]

leos_basement_enemies_metal_only: list[EnemyType] = [
    EnemyType.ACT5_METAL_MOUSE,
    EnemyType.ACT5_BULLDOZER,
    EnemyType.ACT5_HELICOPTER,
]

leos_basement_enemies_no_metal: list[EnemyType] = [EnemyType.ACT5_WORM, EnemyType.ACT5_ROBOT]

model_town_enemies: list[EnemyType] = [
    EnemyType.ACT5_MINI_KNIGHT,
    EnemyType.ACT5_MINI_ARCHER,
    EnemyType.ACT5_MINI_HORSEMAN,
    EnemyType.ACT5_CATAPULT,
    EnemyType.ACT5_TOWER,
]

castle_basement_enemies: list[EnemyType] = [
    EnemyType.ACT6_ORB,
    EnemyType.ACT6_GHOST,
    EnemyType.ACT6_SNAKE,
    EnemyType.ACT6_SKELETON,
]

castle_basement_enemies_no_ghost: list[EnemyType] = [EnemyType.ACT6_ORB, EnemyType.ACT6_SNAKE, EnemyType.ACT6_SKELETON]

castle_basement_enemies_full: list[EnemyType] = [
    EnemyType.ACT6_SKULL,
    EnemyType.ACT6_ORB,
    EnemyType.ACT6_GHOST,
    EnemyType.ACT6_SNAKE,
    EnemyType.ACT6_FIRE,
    EnemyType.ACT6_SKELETON,
]

castle_tower_enemies: list[EnemyType] = [
    EnemyType.ACT6_PURPLE_KNIGHT,
    EnemyType.ACT6_RED_KNIGHT,
    EnemyType.ACT6_MIMIC,
    EnemyType.ACT6_DOLL,
    EnemyType.ACT6_CHESS_KNIGHT,
]

castle_tower_enemies_full: list[EnemyType] = [
    EnemyType.ACT6_PURPLE_KNIGHT,
    EnemyType.ACT6_RED_KNIGHT,
    EnemyType.ACT6_FIRE2,
    EnemyType.ACT6_SKULL2,
    EnemyType.ACT6_MIMIC,
    EnemyType.ACT6_DOLL,
    EnemyType.ACT6_CHESS_KNIGHT,
]

world_of_evil_enemies: list[EnemyType] = [EnemyType.ACT7_DEMON, EnemyType.ACT7_FLY, EnemyType.ACT7_BRICK]

world_of_evil_enemies_no_brick: list[EnemyType] = [EnemyType.ACT7_DEMON, EnemyType.ACT7_FLY]

orientations: list[int] = [
    0x00,  # down
    0x40,  # left
    0x80,  # right
    0xC0,  # up
]

orientations_no_up: list[int] = [
    0x00,  # down
    0x40,  # left
    0x80,  # right
]

randomizable_lair_types: list[LairBehavior] = [
    LairBehavior.ONE_BY_ONE,
    LairBehavior.MULTISPAWN,
    LairBehavior.ONE_BY_ONE_PROX,
    LairBehavior.TWO_UP_TWO_DOWN,
]

randomizable_lair_weights: list[int] = [
    4,
    15,
    1,
    15,
]

randomizable_lair_types_no_two_up: list[LairBehavior] = [
    LairBehavior.ONE_BY_ONE,
    LairBehavior.MULTISPAWN,
    LairBehavior.ONE_BY_ONE_PROX,
]

randomizable_lair_weights_no_two_up: list[int] = [
    4,
    15,
    1,
]

NB_ENEMIES_ONE_BY_ONE_MIN = 2
NB_ENEMIES_ONE_BY_ONE_MAX = 6
NB_ENEMIES_MULTISPAWN_MIN = 4
NB_ENEMIES_MULTISPAWN_MAX = 12
NB_ENEMIES_MULTISPAWN_REDUCED_MIN = 4
NB_ENEMIES_MULTISPAWN_REDUCED_MAX = 8

SPAWN_RATE_MIN = 0x03
SPAWN_RATE_MAX = 0x20
SPAWN_RATE_SLOW_ADJUST = 0x10


def can_randomize_orientation(act: LairAct, enemy: EnemyType) -> bool:
    return (
        (act == LairAct.GREENWOOD and enemy == EnemyType.ACT2_WATER_DRAGON)
        or (act == LairAct.MOUNTAIN_OF_SOULS and enemy == EnemyType.ACT4_RAT)
        or (act == LairAct.MOUNTAIN_OF_SOULS and enemy == EnemyType.ACT4_SNOWBALL)
        or (act == LairAct.LEOS_LAB and enemy == EnemyType.ACT5_METAL_MOUSE)
        or (act == LairAct.LEOS_LAB and enemy == EnemyType.ACT5_ROBOT)
        or (act == LairAct.LEOS_LAB and enemy == EnemyType.ACT5_WORM)
        or (act == LairAct.LEOS_LAB and enemy == EnemyType.ACT5_TOWER)
        or (act == LairAct.MAGRIDD_CASTLE and enemy == EnemyType.ACT6_SKULL)
        or (act == LairAct.MAGRIDD_CASTLE and enemy == EnemyType.ACT6_SNAKE)
        or (act == LairAct.MAGRIDD_CASTLE and enemy == EnemyType.ACT6_SKULL2)
        or (act == LairAct.WORLD_OF_EVIL and enemy == EnemyType.ACT7_BRICK)
    )


def should_slow_down_spawn_enemy(act: LairAct, enemy: EnemyType) -> bool:
    return (
        (act == LairAct.GRASS_VALLEY and enemy == EnemyType.ACT1_PLANT)
        or (act == LairAct.GREENWOOD and enemy == EnemyType.ACT2_FLOWER)
        or (act == LairAct.GREENWOOD and enemy == EnemyType.ACT2_BUSH)
        or (act == LairAct.GREENWOOD and enemy == EnemyType.ACT2_STATUE)
        or (act == LairAct.MOUNTAIN_OF_SOULS and enemy == EnemyType.ACT4_ICE_HEAD)
        or (act == LairAct.LEOS_LAB and enemy == EnemyType.ACT5_MINI_ARCHER)
        or (act == LairAct.LEOS_LAB and enemy == EnemyType.ACT5_CATAPULT)
        or (act == LairAct.LEOS_LAB and enemy == EnemyType.ACT5_BULLDOZER)
    )


def randomize_lair_enemies(random: Random, lair: LairDataRaw, lair_id: int) -> LairDataRaw:
    """Randomize the enemies spawned by a lair."""

    # Don't randomize enemies from 2-up-2-down lairs, because upside-down enemies can sometimes get away...
    if lair.lair_behavior_pointer == LairBehavior.TWO_UP_TWO_DOWN:
        return lair

    # A few lairs should not be randomized (yet)
    if lair_id in must_not_enemize_lair_ids:
        return lair

    enemy = lair.entity_id

    match lair.act_id:
        case LairAct.GRASS_VALLEY:
            if enemy == EnemyType.ACT1_SPIKEY or enemy == EnemyType.SOLID_ARM:
                return lair
            pool = underground_castle_enemies if enemy < EnemyType.ACT1_ARMOR else leos_paintings_enemies

        case LairAct.GREENWOOD:
            if (
                enemy == EnemyType.ACT2_SCORPION
                or enemy == EnemyType.ACT2_FIRE_SPIRIT
                or enemy == EnemyType.ELEMENTAL_STATUE
            ):
                return lair
            pool = (
                water_shrine_enemies if enemy < EnemyType.ACT2_FIRE_SPIRIT else fire_light_shrine_enemies_no_fire_spirit
            )

        case LairAct.ST_ELLES:
            if enemy == EnemyType.ACT3_METAL_GORILLA or enemy == EnemyType.FLOATING_SKULL:
                return lair
            pool = (
                seabed_enemies
                if enemy < EnemyType.ACT3_PALM_TREE
                else island_enemies_no_fish if lair_id in no_fish_lair_ids else island_enemies
            )

        case LairAct.MOUNTAIN_OF_SOULS:
            if enemy == EnemyType.POSEIDON:
                return lair
            pool = (
                mountain_enemies_no_snowball
                if enemy < EnemyType.ACT4_PURPLE_WIZARD
                else laynole_lune_enemies_no_ice_block
            )

        case LairAct.LEOS_LAB:
            if enemy == EnemyType.TIN_DOLL:
                return lair
            pool = (
                model_town_enemies
                if enemy >= EnemyType.ACT5_MINI_KNIGHT
                else (
                    leos_basement_enemies_no_metal
                    if lair_id in no_metal_lair_ids
                    else (
                        leos_basement_enemies_metal_only if lair_id in must_be_metal_lair_ids else leos_basement_enemies
                    )
                )
            )

        case LairAct.MAGRIDD_CASTLE:
            if enemy == EnemyType.DEMON_BIRD:
                return lair
            pool = (
                castle_tower_enemies
                if enemy >= EnemyType.ACT6_PURPLE_KNIGHT
                else (
                    castle_basement_enemies_no_ghost
                    if lair_id in no_ghost_lair_ids
                    else [EnemyType.ACT6_GHOST] if lair_id in must_be_ghost_lair_ids else castle_basement_enemies
                )
            )

        case LairAct.WORLD_OF_EVIL:
            pool = world_of_evil_enemies_no_brick

        case _:
            return lair

    enemy = int(random.choice(pool))

    orientation = lair.orientation

    if can_randomize_orientation(lair.act_id, enemy):
        orientation = (
            random.choice(orientations_no_up)
            if lair_id in must_not_be_upwards_lair_ids
            else random.choice(orientations)
        )
    else:
        orientation = 0x00

    return lair._replace(entity_id=enemy, orientation=orientation)


def randomize_lair_type(random: Random, lair: LairDataRaw) -> LairDataRaw:
    lair_type = lair.lair_behavior_pointer

    if lair_type in randomizable_lair_types_no_two_up:
        lair_type = int(random.choices(randomizable_lair_types_no_two_up, randomizable_lair_weights_no_two_up)[0])
    elif lair_type == LairBehavior.TWO_UP_TWO_DOWN:
        lair_type = int(random.choices(randomizable_lair_types, randomizable_lair_weights)[0])
    else:
        return lair

    return lair._replace(lair_behavior_pointer=lair_type)


def randomize_lair_number_enemies(random: Random, lair: LairDataRaw) -> LairDataRaw:
    num_enemies = lair.enemy_count

    if (
        lair.lair_behavior_pointer == LairBehavior.ONE_BY_ONE
        or lair.lair_behavior_pointer == LairBehavior.ONE_BY_ONE_PROX
    ):
        num_enemies = random.randrange(NB_ENEMIES_ONE_BY_ONE_MIN, NB_ENEMIES_ONE_BY_ONE_MAX)
    elif (
        lair.lair_behavior_pointer == LairBehavior.MULTISPAWN
        or lair.lair_behavior_pointer == LairBehavior.TWO_UP_TWO_DOWN
    ):
        if lair.entity_id == EnemyType.ACT6_MIMIC:
            num_enemies = random.randrange(NB_ENEMIES_MULTISPAWN_REDUCED_MIN, NB_ENEMIES_MULTISPAWN_REDUCED_MAX)
        else:
            num_enemies = random.randrange(NB_ENEMIES_MULTISPAWN_MIN, NB_ENEMIES_MULTISPAWN_REDUCED_MAX)
    else:
        return lair

    return lair._replace(enemy_count=num_enemies)


def randomize_lair_spawn_rate(random: Random, lair: LairDataRaw) -> LairDataRaw:
    spawn_rate = lair.spawn_rate

    if (
        lair.lair_behavior_pointer == LairBehavior.MULTISPAWN
        or lair.lair_behavior_pointer == LairBehavior.TWO_UP_TWO_DOWN
    ):
        spawn_rate = random.randrange(SPAWN_RATE_MIN, SPAWN_RATE_MAX)
        if should_slow_down_spawn_enemy(lair.act_id, lair.entity_id):
            spawn_rate += SPAWN_RATE_SLOW_ADJUST
    else:
        return lair

    if lair.lair_behavior_pointer == LairBehavior.ONE_BY_ONE or lair.lair_behavior_pointer == LairBehavior.ONE_BY_ONE_PROX:
        spawn_rate = 0

    return lair._replace(spawn_rate=spawn_rate)


def randomize_prespawned_enemies(random: Random):
    # TODO: port this functionality.
    pass


def randomize_lair(world: "SoulBlazerWorld", lair: LairDataRaw, lair_id: int) -> LairDataRaw:
    if lair.entity_id == EnemyType.NO_ENEMY or lair.entity_id == EnemyType.DREAM_NO_ENEMY:
        return lair

    if world.options.randomize_lair_enemies:
        lair = randomize_lair_enemies(world.random, lair, lair_id)
    if world.options.randomize_lair_type:
        lair = randomize_lair_type(world.random, lair)
    if world.options.randomize_lair_number_of_enemies:
        lair = randomize_lair_number_enemies(world.random, lair)
    if world.options.randomize_lair_spawn_rate:
        lair = randomize_lair_spawn_rate(world.random, lair)
    return lair


def randomize_world_lairs(world: "SoulBlazerWorld") -> list[LairDataRaw]:
    return [randomize_lair(world, lair, lair_id) for lair_id, lair in enumerate(lair_data)]
