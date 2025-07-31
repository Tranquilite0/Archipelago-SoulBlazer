from dataclasses import dataclass
from Options import Toggle, Range, Choice, PerGameCommonOptions, OptionGroup


class TextSpeed(Choice):
    """
    Text Speed.
    Instant: Text renders an entire window at a time.
    Fast: Text renders a character at a time at the same speed as the JP version.
    """

    display_name: str = "Text Speed"
    option_fast: int = 1
    option_instant: int = 0
    default: int = 0


class Goal(Choice):
    """
    How you beat the game.
    Deathtoll: Defeat Deathtoll.
    Emblem Hunt: Collect all 8 master's emblems and turn them in at the Gem Fairy in Greenwood.
    """

    display_name: str = "Goal"
    option_deathtoll: int = 0
    option_emblem_hunt: int = 1
    default: int = 0


class ActProgression(Choice):
    """
    Act/World progression.
    Vanilla: Talk to town leaders to open the next Act/World.
    Open: All worlds are open from the start of the game.
    """

    display_name: str = "Act Progression"
    option_vanilla: int = 0
    option_open: int = 1
    default: int = 0


class StonesPlacement(Choice):
    """
    Determines the placement of the 6 stones needed to enter the World of Evil.
    Vanilla: Stones are given by the town leader of each act.
    Bosses: Stones are rewarded from the boss lair of each act.
    Totally Random: Stones are randomized with everything else.
    """

    display_name: str = "Stones Placement"
    option_vanilla: int = 0
    option_bosses: int = 1
    option_totally_random: int = 2
    default: int = 0


class StonesCount(Range):
    """
    Number of Stones needed to open the World of Evil.
    """

    display_name: str = "Stones Count"
    range_start: int = 0
    range_end: int = 6
    default: int = 6


class OpenDeathToll(Toggle):
    """
    Determines if Deathtoll's Palace in the World of Evil is already open.
    """

    display_name: str = "Open Deathtoll"


class StartingSword(Choice):
    """
    Determines the sword you will get in the first chest.
    Vanilla: You will get the Sword of Life.
    <Sword Name>: You will get that sword.
    Randomized: You will get a random sword.
    """

    display_name: str = "Starting Sword"

    option_vanilla: int = 0
    option_psycho_sword: int = 1
    option_critical_sword: int = 2
    option_lucky_blade: int = 3
    option_zantetsu_sword: int = 4
    option_spirit_sword: int = 5
    option_recovery_sword: int = 6
    option_soul_blade: int = 7
    option_randomized: int = 8

    default: int = 0


class EquipmentStats(Choice):
    """
    Determines equipment power & defense.
    Vanilla: No change to the way Weapons/Armor work.
    Semi-progressive: Equipment strength/defense scales with the number of swords/armors obtained.
    Shuffle: Shuffles the stats of all swords and armor.
    """

    display_name: str = "Equipment Stats"
    option_vanilla: int = 0
    option_semi_progressive: int = 1
    option_shuffle: int = 2
    default: int = 1


class EquipmentScaling(Choice):
    """
    Determines the stat progression for swords/armor.
    Vanilla: Swords/Armor follow the vanilla 1/2/3/4/6/8/10/12 strength/defense progression.
    Improved: Swords/Armor follow an improved 1/3/5/7/9/12/12/12 strength/defense progression.
    Strong: Swords/Armor follow a strong 2/4/6/9/12/12/12/12 strength/defense progression.
    Weak: Swords/Armor follow a weak 1/1/2/2/3/4/5/6 strength/defense progression.
    Broken: Swords/Armor strength is set to 1/1/1/1/1/1/1/1 strength/defense progression.
    """

    display_name: str = "Equipment Scaling"
    option_vanilla: int = 0
    option_improved: int = 1
    option_strong: int = 2
    option_weak: int = 3
    option_broken: int = 4
    default: int = 0


class MagicianItem(Choice):
    """
    Determines the item the Magician gives you at the start of the game.
    Vanilla: The vanilla reward (Flame Ball).
    Random Spell: A random castable magic spell.
    Totally Random: Any reward in the item pool.
    """

    display_name: str = "Magician's Item"
    option_vanilla: int = 0
    option_random_spell: int = 1
    option_totally_random: int = 2
    default: int = 1


class MagicianSoul(Choice):
    """
    Determines what reward you will get in place of the Magician's Soul at the start of the game.
    Vanilla: You get the Soul of Magician.
    Random Soul: Any progression soul. (Soul of Magician, Soul of Light, Soul of Detection)
    Totally Random: Any reward in the item pool.
    """

    display_name: str = "Magician's Soul"
    option_vanilla: int = 0
    option_random_soul: int = 1
    option_totally_random: int = 2
    default: int = 0


class GemExpPool(Choice):
    """
    Modifies the Gem/Exp rewards in the item pool.
    Vanilla: The same Gem/Exp values as the vanilla game.
    Improved: Gem rewards in the item pool are multiplied by 2, and Exp rewards by 10.
    Random Range: Gem rewards in the pool are randomized in the range of 1-999, and Exp rewards in the range of 1-9999.
    """

    display_name: str = "Gem/Exp Pool"
    option_vanilla: int = 0
    option_improved: int = 1
    option_random_range: int = 2
    default: int = 2


class LairEnemies(Toggle):
    """
    Randomize enemies spawned from lairs.
    """

    display_name: str = "Randomize Lair Enemies"


class LairType(Toggle):
    """
    Randomize how lairs spawn enemies (multi-spawn, one-by-one, proximity, etc).
    """

    display_name: str = "Randomize Lair Type"


class LairNumberOfEnemiesType(Toggle):
    """
    Randomize number of enemies spawned from lairs.
    """

    display_name: str = "Randomize Lair Number of Enemies"


class LairSpawnRate(Choice):
    """
    Randomize how fast enemies are spawned from lairs.
    """

    display_name: str = "Randomize Lair Spawn Rate"
    option_vanilla: int = 0
    option_random: int = 1
    option_random_quick: int = 2
    option_random_hyper: int = 3
    default: int = 0


class PreSpawnedEnemies(Toggle):
    """
    Randomize pre-spawned enemies which are already on the map.
    **Not currently implemented!**
    """

    display_name: str = "Randomize Pre-Spawned Enemies"


# By convention, we call the options dataclass `<world>Options`.
# It has to be derived from 'PerGameCommonOptions'.
@dataclass
class SoulBlazerOptions(PerGameCommonOptions):
    goal: Goal
    act_progression: ActProgression
    stones_placement: StonesPlacement
    stones_count: StonesCount
    open_deathtoll: OpenDeathToll
    starting_sword: StartingSword
    magician_item: MagicianItem
    magician_soul: MagicianSoul
    text_speed: TextSpeed
    equipment_stats: EquipmentStats
    equipment_scaling: EquipmentScaling
    gem_exp_pool: GemExpPool
    lair_enemies: LairEnemies
    lair_type: LairType
    lair_number_of_enemies: LairNumberOfEnemiesType
    lair_spawn_rate: LairSpawnRate
    pre_spawned_enemies: PreSpawnedEnemies


soulblazer_option_groups: list[OptionGroup] = [
    OptionGroup(
        "World Options",
        [
            Goal,
            ActProgression,
            StonesPlacement,
            StonesCount,
            OpenDeathToll,
            StartingSword,
            MagicianItem,
            MagicianSoul,
        ],
    ),
    OptionGroup(
        "QOL Options",
        [
            TextSpeed,
            EquipmentStats,
            EquipmentScaling,
            GemExpPool,
        ],
    ),
    OptionGroup(
        "Enemizer",
        [
            LairEnemies,
            LairType,
            LairNumberOfEnemiesType,
            LairSpawnRate,
            PreSpawnedEnemies,
        ],
    ),
]
