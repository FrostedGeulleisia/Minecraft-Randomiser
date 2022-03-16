import copy
import sys
import os
import json
import random
from functools import reduce
import operator

itemPool = ["minecraft:stone", "minecraft:granite", "minecraft:polished_granite", "minecraft:diorite","minecraft:polished_diorite",
            "minecraft:andesite", "minecraft:polished_andesite", "minecraft:deepslate", "minecraft:cobbled_deepslate",
            "minecraft:polished_deepslate", "minecraft:calcite", "minecraft:tuff", "minecraft:dripstone_block", "minecraft:grass_block",
            "minecraft:dirt", "minecraft:coarse_dirt", "minecraft:podzol", "minecraft:rooted_dirt", "minecraft:crimson_nylium",
            "minecraft:warped_nylium", "minecraft:cobblestone", "minecraft:oak_planks", "minecraft:spruce_planks", "minecraft:birch_planks",
            "minecraft:jungle_planks", "minecraft:acacia_planks", "minecraft:dark_oak_planks", "minecraft:crimson_planks",
            "minecraft:warped_planks", "minecraft:oak_sapling", "minecraft:spruce_sapling", "minecraft:birch_sapling", "minecraft:jungle_sapling",
            "minecraft:acacia_sapling", "minecraft:dark_oak_sapling", "minecraft:bedrock", "minecraft:sand", "minecraft:red_sand",
            "minecraft:gravel", "minecraft:coal_ore", "minecraft:deepslate_coal_ore", "minecraft:iron_ore", "minecraft:deepslate_iron_ore",
            "minecraft:copper_ore", "minecraft:deepslate_copper_ore", "minecraft:gold_ore", "minecraft:deepslate_gold_ore",
            "minecraft:redstone_ore", "minecraft:deepslate_redstone_ore", "minecraft:emerald_ore", "minecraft:deepslate_emerald_ore",
            "minecraft:lapis_ore", "minecraft:deepslate_lapis_ore", "minecraft:diamond_ore", "minecraft:deepslate_diamond_ore",
            "minecraft:nether_gold_ore", "minecraft:nether_quartz_ore", "minecraft:ancient_debris", "minecraft:coal_block",
            "minecraft:raw_iron_block", "minecraft:raw_copper_block", "minecraft:raw_gold_block", "minecraft:amethyst_block",
            "minecraft:budding_amethyst", "minecraft:iron_block", "minecraft:copper_block", "minecraft:gold_block", "minecraft:diamond_block",
            "minecraft:netherite_block", "minecraft:exposed_copper", "minecraft:weathered_copper", "minecraft:oxidized_copper",
            "minecraft:cut_copper", "minecraft:exposed_cut_copper", "minecraft:weathered_cut_copper", "minecraft:oxidized_cut_copper",
            "minecraft:cut_copper_stairs", "minecraft:exposed_cut_copper_stairs", "minecraft:weathered_cut_copper_stairs",
            "minecraft:oxidized_cut_copper_stairs", "minecraft:cut_copper_slab", "minecraft:exposed_cut_copper_slab",
            "minecraft:weathered_cut_copper_slab", "minecraft:oxidized_cut_copper_slab", "minecraft:waxed_copper_block",
            "minecraft:waxed_exposed_copper", "minecraft:waxed_weathered_copper", "minecraft:waxed_oxidized_copper", "minecraft:waxed_cut_copper",
            "minecraft:waxed_exposed_cut_copper", "minecraft:waxed_weathered_cut_copper", "minecraft:waxed_oxidized_cut_copper",
            "minecraft:waxed_cut_copper_stairs", "minecraft:waxed_exposed_cut_copper_stairs", "minecraft:waxed_weathered_cut_copper_stairs",
            "minecraft:waxed_oxidized_cut_copper_stairs", "minecraft:waxed_cut_copper_slab", "minecraft:waxed_exposed_cut_copper_slab",
            "minecraft:waxed_weathered_cut_copper_slab", "minecraft:waxed_oxidized_cut_copper_slab", "minecraft:oak_log",
            "minecraft:spruce_log", "minecraft:birch_log", "minecraft:jungle_log", "minecraft:acacia_log", "minecraft:dark_oak_log",
            "minecraft:crimson_stem", "minecraft:warped_stem", "minecraft:stripped_oak_log", "minecraft:stripped_spruce_log",
            "minecraft:stripped_birch_log", "minecraft:stripped_jungle_log", "minecraft:stripped_acacia_log", "minecraft:stripped_dark_oak_log",
            "minecraft:stripped_crimson_stem", "minecraft:stripped_warped_stem", "minecraft:stripped_oak_wood", "minecraft:stripped_spruce_wood",
            "minecraft:stripped_birch_wood", "minecraft:stripped_jungle_wood", "minecraft:stripped_acacia_wood", "minecraft:stripped_dark_oak_wood",
            "minecraft:stripped_crimson_hyphae", "minecraft:stripped_warped_hyphae", "minecraft:oak_wood", "minecraft:spruce_wood",
            "minecraft:birch_wood", "minecraft:jungle_wood", "minecraft:acacia_wood", "minecraft:dark_oak_wood", "minecraft:crimson_hyphae",
            "minecraft:warped_hyphae", "minecraft:oak_leaves", "minecraft:spruce_leaves", "minecraft:birch_leaves", "minecraft:jungle_leaves",
            "minecraft:acacia_leaves", "minecraft:dark_oak_leaves", "minecraft:azalea_leaves", "minecraft:flowering_azalea_leaves",
            "minecraft:sponge", "minecraft:wet_sponge", "minecraft:glass", "minecraft:tinted_glass", "minecraft:lapis_block",
            "minecraft:sandstone", "minecraft:chiseled_sandstone", "minecraft:cut_sandstone", "minecraft:cobweb", "minecraft:grass",
            "minecraft:fern", "minecraft:azalea", "minecraft:flowering_azalea", "minecraft:dead_bush", "minecraft:seagrass",
            "minecraft:sea_pickle", "minecraft:white_wool", "minecraft:orange_wool", "minecraft:magenta_wool", "minecraft:light_blue_wool",
            "minecraft:yellow_wool", "minecraft:lime_wool", "minecraft:pink_wool", "minecraft:gray_wool", "minecraft:light_gray_wool",
            "minecraft:cyan_wool", "minecraft:purple_wool", "minecraft:blue_wool", "minecraft:brown_wool", "minecraft:green_wool",
            "minecraft:red_wool", "minecraft:black_wool", "minecraft:dandelion", "minecraft:poppy", "minecraft:blue_orchid",
            "minecraft:allium", "minecraft:azure_bluet", "minecraft:red_tulip", "minecraft:orange_tulip", "minecraft:white_tulip",
            "minecraft:pink_tulip", "minecraft:oxeye_daisy", "minecraft:cornflower", "minecraft:lily_of_the_valley", "minecraft:wither_rose",
            "minecraft:spore_blossom", "minecraft:brown_mushroom", "minecraft:red_mushroom", "minecraft:crimson_fungus", "minecraft:warped_fungus",
            "minecraft:crimson_roots", "minecraft:warped_roots", "minecraft:nether_sprouts", "minecraft:weeping_vines", "minecraft:twisting_vines",
            "minecraft:sugar_cane", "minecraft:kelp", "minecraft:moss_carpet", "minecraft:moss_block", "minecraft:hanging_roots",
            "minecraft:big_dripleaf", "minecraft:small_dripleaf", "minecraft:bamboo", "minecraft:oak_slab", "minecraft:spruce_slab",
            "minecraft:birch_slab", "minecraft:jungle_slab", "minecraft:acacia_slab", "minecraft:dark_oak_slab", "minecraft:crimson_slab",
            "minecraft:warped_slab", "minecraft:stone_slab", "minecraft:smooth_stone_slab", "minecraft:sandstone_slab",
            "minecraft:cut_sandstone_slab", "minecraft:petrified_oak_slab", "minecraft:cobblestone_slab", "minecraft:brick_slab",
            "minecraft:stone_brick_slab", "minecraft:nether_brick_slab", "minecraft:quartz_slab", "minecraft:red_sandstone_slab",
            "minecraft:cut_red_sandstone_slab", "minecraft:purpur_slab", "minecraft:prismarine_slab", "minecraft:prismarine_brick_slab",
            "minecraft:dark_prismarine_slab", "minecraft:smooth_quartz", "minecraft:smooth_red_sandstone", "minecraft:smooth_sandstone",
            "minecraft:smooth_stone", "minecraft:bricks", "minecraft:bookshelf", "minecraft:mossy_cobblestone", "minecraft:obsidian",
            "minecraft:torch", "minecraft:end_rod", "minecraft:chorus_plant", "minecraft:chorus_flower", "minecraft:purpur_block",
            "minecraft:purpur_pillar", "minecraft:purpur_stairs", "minecraft:spawner", "minecraft:oak_stairs", "minecraft:chest",
            "minecraft:crafting_table", "minecraft:farmland", "minecraft:furnace", "minecraft:ladder", "minecraft:cobblestone_stairs",
            "minecraft:snow", "minecraft:ice", "minecraft:snow_block", "minecraft:cactus", "minecraft:clay", "minecraft:jukebox",
            "minecraft:oak_fence", "minecraft:spruce_fence", "minecraft:birch_fence", "minecraft:jungle_fence", "minecraft:acacia_fence",
            "minecraft:dark_oak_fence", "minecraft:crimson_fence", "minecraft:warped_fence", "minecraft:pumpkin", "minecraft:carved_pumpkin",
            "minecraft:jack_o_lantern", "minecraft:netherrack", "minecraft:soul_sand", "minecraft:soul_soil", "minecraft:basalt",
            "minecraft:polished_basalt", "minecraft:smooth_basalt", "minecraft:soul_torch", "minecraft:glowstone", "minecraft:infested_stone",
            "minecraft:infested_cobblestone", "minecraft:infested_stone_bricks", "minecraft:infested_mossy_stone_bricks",
            "minecraft:infested_cracked_stone_bricks", "minecraft:infested_chiseled_stone_bricks", "minecraft:infested_deepslate",
            "minecraft:stone_bricks", "minecraft:mossy_stone_bricks", "minecraft:cracked_stone_bricks", "minecraft:chiseled_stone_bricks",
            "minecraft:deepslate_bricks", "minecraft:cracked_deepslate_bricks", "minecraft:deepslate_tiles", "minecraft:cracked_deepslate_tiles",
            "minecraft:chiseled_deepslate", "minecraft:brown_mushroom_block", "minecraft:red_mushroom_block", "minecraft:iron_bars",
            "minecraft:chain", "minecraft:glass_pane", "minecraft:melon", "minecraft:vine", "minecraft:glow_lichen", "minecraft:brick_stairs",
            "minecraft:stone_brick_stairs", "minecraft:mycelium", "minecraft:lily_pad", "minecraft:nether_bricks", "minecraft:cracked_nether_bricks",
            "minecraft:chiseled_nether_bricks", "minecraft:nether_brick_fence", "minecraft:nether_brick_stairs", "minecraft:enchanting_table",
            "minecraft:end_portal_frame", "minecraft:end_stone", "minecraft:end_stone_bricks", "minecraft:dragon_egg", "minecraft:sandstone_stairs",
            "minecraft:ender_chest", "minecraft:emerald_block", "minecraft:spruce_stairs", "minecraft:birch_stairs", "minecraft:jungle_stairs",
            "minecraft:crimson_stairs", "minecraft:warped_stairs", "minecraft:command_block", "minecraft:beacon", "minecraft:cobblestone_wall",
            "minecraft:mossy_cobblestone_wall", "minecraft:brick_wall", "minecraft:prismarine_wall", "minecraft:red_sandstone_wall",
            "minecraft:mossy_stone_brick_wall", "minecraft:granite_wall", "minecraft:stone_brick_wall", "minecraft:nether_brick_wall",
            "minecraft:andesite_wall", "minecraft:red_nether_brick_wall", "minecraft:sandstone_wall", "minecraft:end_stone_brick_wall",
            "minecraft:diorite_wall", "minecraft:blackstone_wall", "minecraft:polished_blackstone_wall", "minecraft:polished_blackstone_brick_wall",
            "minecraft:cobbled_deepslate_wall", "minecraft:polished_deepslate_wall", "minecraft:deepslate_brick_wall", "minecraft:deepslate_tile_wall",
            "minecraft:anvil", "minecraft:chipped_anvil", "minecraft:damaged_anvil", "minecraft:chiseled_quartz_block", "minecraft:quartz_block",
            "minecraft:quartz_bricks", "minecraft:quartz_pillar", "minecraft:quartz_stairs", "minecraft:white_terracotta",
            "minecraft:orange_terracotta", "minecraft:magenta_terracotta", "minecraft:light_blue_terracotta", "minecraft:yellow_terracotta",
            "minecraft:lime_terracotta", "minecraft:pink_terracotta", "minecraft:gray_terracotta", "minecraft:light_gray_terracotta",
            "minecraft:cyan_terracotta", "minecraft:purple_terracotta", "minecraft:blue_terracotta", "minecraft:brown_terracotta",
            "minecraft:green_terracotta", "minecraft:red_terracotta", "minecraft:black_terracotta", "minecraft:barrier",
            "minecraft:light", "minecraft:hay_block", "minecraft:white_carpet", "minecraft:orange_carpet", "minecraft:magenta_carpet",
            "minecraft:light_blue_carpet", "minecraft:yellow_carpet", "minecraft:lime_carpet", "minecraft:pink_carpet", "minecraft:gray_carpet",
            "minecraft:light_gray_carpet", "minecraft:cyan_carpet", "minecraft:purple_carpet", "minecraft:blue_carpet", "minecraft:brown_carpet",
            "minecraft:green_carpet", "minecraft:red_carpet", "minecraft:black_carpet", "minecraft:terracotta", "minecraft:packed_ice",
            "minecraft:acacia_stairs", "minecraft:dark_oak_stairs", "minecraft:dirt_path", "minecraft:sunflower", "minecraft:lilac",
            "minecraft:rose_bush", "minecraft:peony", "minecraft:tall_grass", "minecraft:large_fern", "minecraft:white_stained_glass",
            "minecraft:orange_stained_glass", "minecraft:magenta_stained_glass", "minecraft:light_blue_stained_glass", "minecraft:yellow_stained_glass",
            "minecraft:lime_stained_glass", "minecraft:pink_stained_glass", "minecraft:gray_stained_glass", "minecraft:light_gray_stained_glass",
            "minecraft:cyan_stained_glass", "minecraft:purple_stained_glass", "minecraft:blue_stained_glass", "minecraft:brown_stained_glass",
            "minecraft:green_stained_glass", "minecraft:red_stained_glass", "minecraft:black_stained_glass", "minecraft:white_stained_glass_pane",
            "minecraft:orange_stained_glass_pane", "minecraft:magenta_stained_glass_pane", "minecraft:light_blue_stained_glass_pane",
            "minecraft:yellow_stained_glass_pane", "minecraft:lime_stained_glass_pane", "minecraft:pink_stained_glass_pane",
            "minecraft:gray_stained_glass_pane", "minecraft:light_gray_stained_glass_pane", "minecraft:cyan_stained_glass_pane",
            "minecraft:purple_stained_glass_pane", "minecraft:blue_stained_glass_pane", "minecraft:brown_stained_glass_pane",
            "minecraft:green_stained_glass_pane", "minecraft:red_stained_glass_pane", "minecraft:black_stained_glass_pane",
            "minecraft:prismarine", "minecraft:prismarine_bricks", "minecraft:dark_prismarine", "minecraft:prismarine_stairs",
            "minecraft:prismarine_brick_stairs", "minecraft:dark_prismarine_stairs", "minecraft:sea_lantern", "minecraft:red_sandstone",
            "minecraft:chiseled_red_sandstone", "minecraft:cut_red_sandstone", "minecraft:red_sandstone_stairs", "minecraft:repeating_command_block",
            "minecraft:chain_command_block", "minecraft:magma_block", "minecraft:nether_wart_block", "minecraft:warped_wart_block",
            "minecraft:red_nether_bricks", "minecraft:bone_block", "minecraft:structure_void", "minecraft:shulker_box", "minecraft:white_shulker_box",
            "minecraft:orange_shulker_box", "minecraft:magenta_shulker_box", "minecraft:light_blue_shulker_box", "minecraft:yellow_shulker_box",
            "minecraft:lime_shulker_box", "minecraft:pink_shulker_box", "minecraft:gray_shulker_box", "minecraft:light_gray_shulker_box",
            "minecraft:cyan_shulker_box", "minecraft:purple_shulker_box", "minecraft:blue_shulker_box", "minecraft:brown_shulker_box",
            "minecraft:green_shulker_box", "minecraft:red_shulker_box", "minecraft:black_shulker_box", "minecraft:white_glazed_terracotta",
            "minecraft:orange_glazed_terracotta", "minecraft:magenta_glazed_terracotta", "minecraft:light_blue_glazed_terracotta",
            "minecraft:yellow_glazed_terracotta", "minecraft:lime_glazed_terracotta", "minecraft:pink_glazed_terracotta",
            "minecraft:gray_glazed_terracotta", "minecraft:light_gray_glazed_terracotta", "minecraft:cyan_glazed_terracotta",
            "minecraft:purple_glazed_terracotta", "minecraft:blue_glazed_terracotta", "minecraft:brown_glazed_terracotta",
            "minecraft:green_glazed_terracotta", "minecraft:red_glazed_terracotta", "minecraft:black_glazed_terracotta",
            "minecraft:white_concrete", "minecraft:orange_concrete", "minecraft:magenta_concrete", "minecraft:light_blue_concrete",
            "minecraft:yellow_concrete", "minecraft:lime_concrete", "minecraft:pink_concrete", "minecraft:gray_concrete",
            "minecraft:light_gray_concrete", "minecraft:cyan_concrete", "minecraft:purple_concrete", "minecraft:blue_concrete",
            "minecraft:brown_concrete", "minecraft:green_concrete", "minecraft:red_concrete", "minecraft:black_concrete",
            "minecraft:white_concrete_powder", "minecraft:orange_concrete_powder", "minecraft:magenta_concrete_powder",
            "minecraft:light_blue_concrete_powder", "minecraft:yellow_concrete_powder", "minecraft:lime_concrete_powder",
            "minecraft:pink_concrete_powder", "minecraft:gray_concrete_powder", "minecraft:light_gray_concrete_powder",
            "minecraft:cyan_concrete_powder", "minecraft:purple_concrete_powder", "minecraft:blue_concrete_powder", "minecraft:brown_concrete_powder",
            "minecraft:green_concrete_powder", "minecraft:red_concrete_powder", "minecraft:black_concrete_powder", "minecraft:turtle_egg",
            "minecraft:dead_tube_coral_block", "minecraft:dead_brain_coral_block", "minecraft:dead_bubble_coral_block",
            "minecraft:dead_fire_coral_block", "minecraft:dead_horn_coral_block", "minecraft:tube_coral_block", "minecraft:brain_coral_block",
            "minecraft:bubble_coral_block", "minecraft:fire_coral_block", "minecraft:horn_coral_block", "minecraft:tube_coral",
            "minecraft:brain_coral", "minecraft:bubble_coral", "minecraft:fire_coral", "minecraft:horn_coral", "minecraft:dead_tube_coral",
            "minecraft:dead_brain_coral", "minecraft:dead_bubble_coral", "minecraft:dead_fire_coral", "minecraft:dead_horn_coral",
            "minecraft:tube_coral_fan", "minecraft:brain_coral_fan", "minecraft:bubble_coral_fan", "minecraft:fire_coral_fan",
            "minecraft:horn_coral_fan", "minecraft:dead_tube_coral_fan", "minecraft:dead_brain_coral_fan", "minecraft:dead_bubble_coral_fan",
            "minecraft:dead_fire_coral_fan", "minecraft:dead_horn_coral_fan", "minecraft:blue_ice", "minecraft:conduit",
            "minecraft:polished_granite_stairs", "minecraft:smooth_red_sandstone_stairs", "minecraft:mossy_stone_brick_stairs",
            "minecraft:polished_diorite_stairs", "minecraft:mossy_cobblestone_stairs", "minecraft:end_stone_brick_stairs",
            "minecraft:stone_stairs", "minecraft:smooth_sandstone_stairs", "minecraft:smooth_quartz_stairs", "minecraft:granite_stairs",
            "minecraft:andesite_stairs", "minecraft:red_nether_brick_stairs", "minecraft:polished_andesite_stairs", "minecraft:diorite_stairs",
            "minecraft:cobbled_deepslate_stairs", "minecraft:polished_deepslate_stairs", "minecraft:deepslate_brick_stairs",
            "minecraft:deepslate_tile_stairs", "minecraft:polished_granite_slab", "minecraft:smooth_red_sandstone_slab",
            "minecraft:mossy_stone_brick_slab", "minecraft:polished_diorite_slab", "minecraft:mossy_cobblestone_slab", "minecraft:end_stone_brick_slab",
            "minecraft:smooth_sandstone_slab", "minecraft:smooth_quartz_slab", "minecraft:granite_slab", "minecraft:andesite_slab",
            "minecraft:red_nether_brick_slab", "minecraft:polished_andesite_slab", "minecraft:diorite_slab", "minecraft:cobbled_deepslate_slab",
            "minecraft:polished_deepslate_slab", "minecraft:deepslate_brick_slab", "minecraft:deepslate_tile_slab", "minecraft:scaffolding",
            "minecraft:redstone", "minecraft:redstone_torch", "minecraft:redstone_block", "minecraft:repeater", "minecraft:comparator",
            "minecraft:piston", "minecraft:sticky_piston", "minecraft:slime_block", "minecraft:honey_block", "minecraft:observer",
            "minecraft:hopper", "minecraft:dispenser", "minecraft:dropper", "minecraft:lectern", "minecraft:target", "minecraft:lever",
            "minecraft:lightning_rod", "minecraft:daylight_detector", "minecraft:sculk_sensor", "minecraft:tripwire_hook",
            "minecraft:trapped_chest", "minecraft:tnt", "minecraft:redstone_lamp", "minecraft:note_block", "minecraft:stone_button",
            "minecraft:polished_blackstone_button", "minecraft:oak_button", "minecraft:spruce_button", "minecraft:birch_button",
            "minecraft:jungle_button", "minecraft:acacia_button", "minecraft:dark_oak_button", "minecraft:crimson_button",
            "minecraft:warped_button", "minecraft:stone_pressure_plate", "minecraft:polished_blackstone_pressure_plate",
            "minecraft:light_weighted_pressure_plate", "minecraft:heavy_weighted_pressure_plate", "minecraft:oak_pressure_plate",
            "minecraft:spruce_pressure_plate", "minecraft:birch_pressure_plate", "minecraft:jungle_pressure_plate", "minecraft:acacia_pressure_plate",
            "minecraft:dark_oak_pressure_plate", "minecraft:crimson_pressure_plate", "minecraft:warped_pressure_plate", "minecraft:iron_door",
            "minecraft:oak_door", "minecraft:spruce_door", "minecraft:birch_door", "minecraft:jungle_door", "minecraft:acacia_door",
            "minecraft:dark_oak_door", "minecraft:crimson_door", "minecraft:warped_door", "minecraft:iron_trapdoor", "minecraft:oak_trapdoor",
            "minecraft:spruce_trapdoor", "minecraft:birch_trapdoor", "minecraft:jungle_trapdoor", "minecraft:acacia_trapdoor",
            "minecraft:dark_oak_trapdoor", "minecraft:crimson_trapdoor", "minecraft:warped_trapdoor", "minecraft:oak_fence_gate",
            "minecraft:spruce_fence_gate", "minecraft:birch_fence_gate", "minecraft:jungle_fence_gate", "minecraft:acacia_fence_gate",
            "minecraft:dark_oak_fence_gate", "minecraft:crimson_fence_gate", "minecraft:warped_fence_gate", "minecraft:powered_rail",
            "minecraft:detector_rail", "minecraft:rail", "minecraft:activator_rail", "minecraft:saddle", "minecraft:minecart",
            "minecraft:chest_minecart", "minecraft:furnace_minecart", "minecraft:tnt_minecart", "minecraft:hopper_minecart",
            "minecraft:carrot_on_a_stick", "minecraft:warped_fungus_on_a_stick", "minecraft:elytra", "minecraft:oak_boat",
            "minecraft:spruce_boat", "minecraft:birch_boat", "minecraft:jungle_boat", "minecraft:acacia_boat", "minecraft:dark_oak_boat",
            "minecraft:structure_block", "minecraft:jigsaw", "minecraft:scute", "minecraft:flint_and_steel",
            "minecraft:apple", "minecraft:arrow", "minecraft:coal", "minecraft:charcoal", "minecraft:diamond",
            "minecraft:emerald", "minecraft:lapis_lazuli", "minecraft:quartz", "minecraft:amethyst_shard", "minecraft:raw_iron",
            "minecraft:iron_ingot", "minecraft:raw_copper", "minecraft:copper_ingot", "minecraft:raw_gold", "minecraft:gold_ingot",
            "minecraft:netherite_ingot", "minecraft:netherite_scrap", "minecraft:stick", "minecraft:bowl",
            "minecraft:mushroom_stew", "minecraft:string", "minecraft:feather", "minecraft:gunpowder", "minecraft:wheat_seeds",
            "minecraft:wheat", "minecraft:bread", "minecraft:flint", "minecraft:porkchop", "minecraft:cooked_porkchop", "minecraft:painting",
            "minecraft:golden_apple", "minecraft:enchanted_golden_apple", "minecraft:oak_sign", "minecraft:spruce_sign",
            "minecraft:birch_sign", "minecraft:jungle_sign", "minecraft:acacia_sign", "minecraft:dark_oak_sign", "minecraft:crimson_sign",
            "minecraft:warped_sign", "minecraft:bucket", "minecraft:water_bucket", "minecraft:lava_bucket", "minecraft:powder_snow_bucket",
            "minecraft:snowball", "minecraft:leather", "minecraft:milk_bucket", "minecraft:pufferfish_bucket", "minecraft:salmon_bucket",
            "minecraft:cod_bucket", "minecraft:tropical_fish_bucket", "minecraft:axolotl_bucket", "minecraft:brick", "minecraft:clay_ball",
            "minecraft:dried_kelp_block", "minecraft:paper", "minecraft:slime_ball", "minecraft:egg", "minecraft:compass",
            "minecraft:bundle", "minecraft:clock", "minecraft:spyglass", "minecraft:glowstone_dust",
            "minecraft:cod", "minecraft:salmon", "minecraft:tropical_fish", "minecraft:pufferfish", "minecraft:cooked_cod",
            "minecraft:cooked_salmon", "minecraft:ink_sac", "minecraft:glow_ink_sac", "minecraft:cocoa_beans", "minecraft:white_dye",
            "minecraft:orange_dye", "minecraft:magenta_dye", "minecraft:light_blue_dye", "minecraft:yellow_dye", "minecraft:lime_dye",
            "minecraft:pink_dye", "minecraft:gray_dye", "minecraft:light_gray_dye", "minecraft:cyan_dye", "minecraft:purple_dye",
            "minecraft:blue_dye", "minecraft:brown_dye", "minecraft:green_dye", "minecraft:red_dye", "minecraft:black_dye",
            "minecraft:bone_meal", "minecraft:bone", "minecraft:sugar", "minecraft:cake", "minecraft:white_bed", "minecraft:orange_bed",
            "minecraft:magenta_bed", "minecraft:light_blue_bed", "minecraft:yellow_bed", "minecraft:lime_bed", "minecraft:pink_bed",
            "minecraft:gray_bed", "minecraft:light_gray_bed", "minecraft:cyan_bed", "minecraft:purple_bed", "minecraft:blue_bed",
            "minecraft:brown_bed", "minecraft:green_bed", "minecraft:red_bed", "minecraft:black_bed", "minecraft:cookie",
            "minecraft:filled_map", "minecraft:shears", "minecraft:melon_slice", "minecraft:dried_kelp", "minecraft:pumpkin_seeds",
            "minecraft:melon_seeds", "minecraft:beef", "minecraft:cooked_beef", "minecraft:chicken", "minecraft:cooked_chicken",
            "minecraft:rotten_flesh", "minecraft:ender_pearl", "minecraft:blaze_rod", "minecraft:ghast_tear", "minecraft:gold_nugget",
            "minecraft:nether_wart", "minecraft:spider_eye", "minecraft:fermented_spider_eye", "minecraft:blaze_powder",
            "minecraft:magma_cream", "minecraft:brewing_stand", "minecraft:cauldron", "minecraft:ender_eye", "minecraft:glistering_melon_slice",
            "minecraft:axolotl_spawn_egg", "minecraft:bat_spawn_egg", "minecraft:bee_spawn_egg", "minecraft:blaze_spawn_egg",
            "minecraft:cat_spawn_egg", "minecraft:cave_spider_spawn_egg", "minecraft:chicken_spawn_egg", "minecraft:cod_spawn_egg",
            "minecraft:cow_spawn_egg", "minecraft:creeper_spawn_egg", "minecraft:dolphin_spawn_egg", "minecraft:donkey_spawn_egg",
            "minecraft:drowned_spawn_egg", "minecraft:elder_guardian_spawn_egg", "minecraft:enderman_spawn_egg", "minecraft:endermite_spawn_egg",
            "minecraft:evoker_spawn_egg", "minecraft:fox_spawn_egg", "minecraft:ghast_spawn_egg", "minecraft:glow_squid_spawn_egg",
            "minecraft:goat_spawn_egg", "minecraft:guardian_spawn_egg", "minecraft:hoglin_spawn_egg", "minecraft:horse_spawn_egg",
            "minecraft:husk_spawn_egg", "minecraft:llama_spawn_egg", "minecraft:magma_cube_spawn_egg", "minecraft:mooshroom_spawn_egg",
            "minecraft:mule_spawn_egg", "minecraft:ocelot_spawn_egg", "minecraft:panda_spawn_egg", "minecraft:parrot_spawn_egg",
            "minecraft:phantom_spawn_egg", "minecraft:pig_spawn_egg", "minecraft:piglin_spawn_egg", "minecraft:piglin_brute_spawn_egg",
            "minecraft:pillager_spawn_egg", "minecraft:polar_bear_spawn_egg", "minecraft:pufferfish_spawn_egg", "minecraft:rabbit_spawn_egg",
            "minecraft:ravager_spawn_egg", "minecraft:salmon_spawn_egg", "minecraft:sheep_spawn_egg", "minecraft:shulker_spawn_egg",
            "minecraft:silverfish_spawn_egg", "minecraft:skeleton_spawn_egg", "minecraft:skeleton_horse_spawn_egg", "minecraft:slime_spawn_egg",
            "minecraft:spider_spawn_egg", "minecraft:squid_spawn_egg", "minecraft:stray_spawn_egg", "minecraft:strider_spawn_egg",
            "minecraft:trader_llama_spawn_egg", "minecraft:tropical_fish_spawn_egg", "minecraft:turtle_spawn_egg", "minecraft:vex_spawn_egg",
            "minecraft:villager_spawn_egg", "minecraft:vindicator_spawn_egg", "minecraft:wandering_trader_spawn_egg",
            "minecraft:witch_spawn_egg", "minecraft:wither_skeleton_spawn_egg", "minecraft:wolf_spawn_egg", "minecraft:zoglin_spawn_egg",
            "minecraft:zombie_spawn_egg", "minecraft:zombie_horse_spawn_egg", "minecraft:zombie_villager_spawn_egg",
            "minecraft:zombified_piglin_spawn_egg", "minecraft:experience_bottle", "minecraft:fire_charge", "minecraft:writable_book",
            "minecraft:written_book", "minecraft:item_frame", "minecraft:glow_item_frame", "minecraft:flower_pot", "minecraft:carrot",
            "minecraft:potato", "minecraft:baked_potato", "minecraft:poisonous_potato", "minecraft:map", "minecraft:golden_carrot",
            "minecraft:skeleton_skull", "minecraft:wither_skeleton_skull", "minecraft:player_head", "minecraft:zombie_head",
            "minecraft:creeper_head", "minecraft:dragon_head", "minecraft:nether_star", "minecraft:pumpkin_pie", "minecraft:firework_rocket",
            "minecraft:firework_star", "minecraft:nether_brick", "minecraft:prismarine_shard", "minecraft:prismarine_crystals",
            "minecraft:rabbit", "minecraft:cooked_rabbit", "minecraft:rabbit_stew", "minecraft:rabbit_foot", "minecraft:rabbit_hide",
            "minecraft:armor_stand", "minecraft:iron_horse_armor", "minecraft:golden_horse_armor", "minecraft:diamond_horse_armor",
            "minecraft:leather_horse_armor", "minecraft:lead", "minecraft:name_tag", "minecraft:command_block_minecart",
            "minecraft:mutton", "minecraft:cooked_mutton", "minecraft:white_banner", "minecraft:orange_banner", "minecraft:magenta_banner",
            "minecraft:light_blue_banner", "minecraft:yellow_banner", "minecraft:lime_banner", "minecraft:pink_banner", "minecraft:gray_banner",
            "minecraft:light_gray_banner", "minecraft:cyan_banner", "minecraft:purple_banner", "minecraft:blue_banner", "minecraft:brown_banner",
            "minecraft:green_banner", "minecraft:red_banner", "minecraft:black_banner", "minecraft:end_crystal", "minecraft:chorus_fruit",
            "minecraft:popped_chorus_fruit", "minecraft:beetroot", "minecraft:beetroot_seeds", "minecraft:beetroot_soup",
            "minecraft:dragon_breath", "minecraft:spectral_arrow", "minecraft:shield", "minecraft:totem_of_undying", "minecraft:shulker_shell",
            "minecraft:iron_nugget", "minecraft:knowledge_book", "minecraft:debug_stick", "minecraft:music_disc_13", "minecraft:music_disc_cat",
            "minecraft:music_disc_blocks", "minecraft:music_disc_chirp", "minecraft:music_disc_far", "minecraft:music_disc_mall",
            "minecraft:music_disc_mellohi", "minecraft:music_disc_stal", "minecraft:music_disc_strad", "minecraft:music_disc_ward",
            "minecraft:music_disc_11", "minecraft:music_disc_wait", "minecraft:music_disc_otherside", "minecraft:music_disc_pigstep",
            "minecraft:phantom_membrane", "minecraft:nautilus_shell", "minecraft:heart_of_the_sea",
            "minecraft:suspicious_stew", "minecraft:loom", "minecraft:flower_banner_pattern", "minecraft:creeper_banner_pattern",
            "minecraft:skull_banner_pattern", "minecraft:mojang_banner_pattern", "minecraft:globe_banner_pattern", "minecraft:piglin_banner_pattern",
            "minecraft:composter", "minecraft:barrel", "minecraft:smoker", "minecraft:blast_furnace", "minecraft:cartography_table",
            "minecraft:fletching_table", "minecraft:grindstone", "minecraft:smithing_table", "minecraft:stonecutter", "minecraft:bell",
            "minecraft:lantern", "minecraft:soul_lantern", "minecraft:sweet_berries", "minecraft:glow_berries", "minecraft:campfire",
            "minecraft:soul_campfire", "minecraft:shroomlight", "minecraft:honeycomb", "minecraft:bee_nest", "minecraft:beehive",
            "minecraft:honey_bottle", "minecraft:honeycomb_block", "minecraft:lodestone", "minecraft:crying_obsidian", "minecraft:blackstone",
            "minecraft:blackstone_slab", "minecraft:blackstone_stairs", "minecraft:gilded_blackstone", "minecraft:polished_blackstone",
            "minecraft:polished_blackstone_slab", "minecraft:polished_blackstone_stairs", "minecraft:chiseled_polished_blackstone",
            "minecraft:polished_blackstone_bricks", "minecraft:polished_blackstone_brick_slab", "minecraft:polished_blackstone_brick_stairs",
            "minecraft:cracked_polished_blackstone_bricks", "minecraft:respawn_anchor", "minecraft:candle", "minecraft:white_candle",
            "minecraft:orange_candle", "minecraft:magenta_candle", "minecraft:light_blue_candle", "minecraft:yellow_candle",
            "minecraft:lime_candle", "minecraft:pink_candle", "minecraft:gray_candle", "minecraft:light_gray_candle", "minecraft:cyan_candle",
            "minecraft:purple_candle", "minecraft:blue_candle", "minecraft:brown_candle", "minecraft:green_candle", "minecraft:red_candle",
            "minecraft:black_candle", "minecraft:small_amethyst_bud", "minecraft:medium_amethyst_bud", "minecraft:large_amethyst_bud",
            "minecraft:pointed_dripstone"]
ENCHANTPOOL = ["minecraft:turtle_helmet","minecraft:leather_helmet","minecraft:leather_chestplate","minecraft:leather_leggings",
            "minecraft:leather_boots","minecraft:chainmail_helmet","minecraft:chainmail_chestplate","minecraft:chainmail_leggings","minecraft:chainmail_boots",
            "minecraft:iron_helmet","minecraft:iron_chestplate","minecraft:iron_leggings","minecraft:iron_boots","minecraft:diamond_helmet",
            "minecraft:diamond_chestplate","minecraft:diamond_leggings","minecraft:diamond_boots","minecraft:golden_helmet","minecraft:golden_chestplate",
            "minecraft:golden_leggings","minecraft:golden_boots","minecraft:netherite_helmet","minecraft:netherite_chestplate","minecraft:netherite_leggings",
            "minecraft:netherite_boots","minecraft:wooden_sword","minecraft:wooden_shovel","minecraft:wooden_pickaxe","minecraft:wooden_axe",
            "minecraft:wooden_hoe","minecraft:stone_sword","minecraft:stone_shovel","minecraft:stone_pickaxe","minecraft:stone_axe","minecraft:stone_hoe",
            "minecraft:golden_sword","minecraft:golden_shovel","minecraft:golden_pickaxe","minecraft:golden_axe","minecraft:golden_hoe",
            "minecraft:iron_sword","minecraft:iron_shovel","minecraft:iron_pickaxe","minecraft:iron_axe","minecraft:iron_hoe","minecraft:diamond_sword",
            "minecraft:diamond_shovel","minecraft:diamond_pickaxe","minecraft:diamond_axe","minecraft:diamond_hoe","minecraft:netherite_sword",
            "minecraft:netherite_shovel","minecraft:netherite_pickaxe","minecraft:netherite_axe","minecraft:netherite_hoe","minecraft:trident",
            "minecraft:bow","minecraft:crossbow","minecraft:fishing_rod", "minecraft:book",]
POTIONPOOL = ["minecraft:potion", "minecraft:tipped_arrow", "minecraft:splash_potion", "minecraft:lingering_potion"]
taggedPool = []
TAGPOOL = ["minecraft:anvil", "minecraft:arrows", "minecraft:banners", "minecraft:beds", "minecraft:boats", "minecraft:buttons",
           "minecraft:candles", "minecraft:carpets", "minecraft:coal_ores", "minecraft:coals", "minecraft:copper_ores", 
           "minecraft:diamond_ores", "dirt", "minecraft:doors", "minecraft:emerald_ores", "minecraft:fences", "minecraft:gold_ores", 
           "minecraft:iron_ores", "minecraft:lapis_ores", "minecraft:leaves", "minecraft:logs", "minecraft:planks", 
           "minecraft:rails", "minecraft:redstone_ores", "minecraft:sand", "minecraft:saplings", "minecraft:signs", 
           "minecraft:slabs", "minecraft:small_flowers", "minecraft:stairs", "minecraft:stone_bricks", "minecraft:tall_flowers",
           "minecraft:terracotta", "minecraft:trapdoors", "minecraft:walls", "minecraft:wool"]
POTIONEFFECTS = ["minecraft:empty","minecraft:water","minecraft:mundane","minecraft:thick","minecraft:awkward","minecraft:night_vision",
            "minecraft:long_night_vision","minecraft:invisibility","minecraft:long_invisibility","minecraft:leaping","minecraft:strong_leaping",
            "minecraft:long_leaping","minecraft:fire_resistance","minecraft:long_fire_resistance","minecraft:swiftness",
            "minecraft:strong_swiftness","minecraft:long_swiftness","minecraft:slowness","minecraft:strong_slowness","minecraft:long_slowness",
            "minecraft:water_breathing","minecraft:long_water_breathing","minecraft:healing","minecraft:strong_healing",
            "minecraft:harming","minecraft:strong_harming","minecraft:poison","minecraft:strong_poison","minecraft:long_poison",
            "minecraft:regeneration","minecraft:strong_regeneration","minecraft:long_regeneration","minecraft:strength",
            "minecraft:strong_strength","minecraft:long_strength","minecraft:weakness","minecraft:long_weakness","minecraft:luck",
            "minecraft:turtle_master","minecraft:strong_turtle_master","minecraft:long_turtle_master","minecraft:slow_falling",
            "minecraft:long_slow_falling"]

def processDir(path):
    returnDir = {}
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                if entry.name.endswith(".json"):
                    with open(entry.path, 'r') as file:
                        returnDir[entry.name] = json.load(file)
            elif entry.is_dir():
                returnDir[entry.name] = processDir(path+entry.name+"/")
    return returnDir

def processNewTag(name):
    JSON = inputJSONs[name]
    processTag(JSON)

def processTag(JSON):
    for value in JSON["values"]:
        if value.startswith("#"):
            processNewTag(value.split(":")[1] + ".json")
        elif value in itemPool:
            taggedPool.append(value)
            itemPool.remove(value)

def processPools(pool, stack):
    stack.append("entries")
    listFor(pool["entries"], stack, processEntries)
    del stack[-1]

def processEntries(entry, stack):
    if entry["type"] == "minecraft:item":
        processEntry(entry, stack)
    elif "children" in entry:
        stack.append("children")
        listFor(entry["children"], stack, processEntries)
        del stack[-1]

def processEntry(entry, stack):
    drop = takeRandomFromPool(normPool, normBasePool)
    stack.append("name")
    setWithStack(drop, stack)
    del stack[-1]
    if "functions" in entry:
        stack.append("functions")
        indexMod = 0
        for index, func in enumerate(entry["functions"]):
            if func["function"] == "minecraft:enchant_with_levels" or func["function"] == "minecraft:enchant_randomly" or func["function"] == "minecraft:set_potion":
                delWithStack(index-indexMod, stack)
                indexMod = indexMod+1
        if drop in ENCHANTPOOL:
            setEnchantment(stack)
        if drop in POTIONPOOL:
            setPotion(stack)
        deleteListOfDictsIfEmpty(stack)
        del stack[-1]

def processRecipeResult(stack):
    drop = takeRandomFromPool(normPool, normBasePool)
    stack.append("result")
    setWithStack(drop, stack)
    del stack[-1]

def setEnchantment(stack):
    if random.random() > 0.5:
        funcDict={"function": "minecraft:enchant_with_levels", "levels": random.randrange(1, 30)}
        if random.random() > 0.5:
            funcDict["treasure"] = True
        else:
            funcDict["treasure"] = False
        reduce(operator.getitem, stack, outputJSONs).append(funcDict)

def setPotion(stack):
    reduce(operator.getitem, stack, outputJSONs).append({"function": "minecraft:set_potion", "id": random.choice(POTIONEFFECTS)})

def deleteListOfDictsIfEmpty(stack):
    if reduce(operator.getitem, stack, outputJSONs) == []:
        del reduce(operator.getitem, stack[:-1], outputJSONs)[stack[-1]]

def takeRandomFromPool(pool, basePool):
    if pool == []:
        pool = copy.deepcopy(basePool)
    choice = random.choice(pool)
    pool.remove(choice)
    return choice

def processLootTable(JSON, stack):
    if "pools" in JSON:
        stack.append("pools")
        listFor(JSON["pools"], stack, processPools)
        del stack[-1]

def processLootTables(jsons, stack):
    dictFor(jsons, stack, processLootTable)

def processRecipeIngredient(_, stack):
    drop = takeRandomFromPool(ingPool, ingBasePool)
    if drop in TAGPOOL:
        setWithStack({"tag": drop}, stack)
    else:
        setWithStack({"item": drop}, stack)

def listFor(list, stack, funcToRun):
    for index, entry in enumerate(list):
        stack.append(index)
        funcToRun(entry,stack)
        del stack[-1]

def dictFor(dict, stack, funcToRun):
    for key, value in dict.items():
        print(key)
        stack.append(key)
        funcToRun(value, stack)
        del stack[-1]

def listOfdictFor(listofdict, stack, funcToRun):
    for num, dict in enumerate(listofdict):
        stack.append(num)
        dictFor(dict, stack, funcToRun)
        del stack[-1]

def dictForDictFor(dict, stack, funcToRun):
    for key, dict in dict.items():
        stack.append(key)
        dictFor(dict, stack, funcToRun)
        del stack[-1]

def setWithStack(var, stack):
    operator.setitem(reduce(operator.getitem, stack[:-1], outputJSONs), stack[-1], var)

def delWithStack(index, stack):
    del reduce(operator.getitem, stack, outputJSONs)[index]

def formItemPool(base,tagged,tags):
    basePool = []
    if base:
        basePool = itemPool + ENCHANTPOOL
    if tagged:
        basePool = basePool + taggedPool
    if tags:
        basePool = basePool + TAGPOOL
    pool = copy.deepcopy(basePool)
    return pool, basePool

def saveFolder(folder, location):
    for name, file in folder.items():
        saveLoc = os.path.join(location,name)
        if name.endswith(".json"):
            jsonToSave = json.dumps(file, indent=2)
            with open(saveLoc, "w") as outfile:
                outfile.write(jsonToSave)
        else:
            print(saveLoc)
            if not os.path.isdir(saveLoc):
                os.mkdir(saveLoc)
            saveFolder(file, saveLoc)

toggles = ["reciperesult", "recipeingredients", "blockdrops", "chestcontents", "entitydrops", "piglinbarter", "fishing", "herogifts", "catgifts","smithingbase","smithingaddition","smithingresult"]
enabled = {}

for setting in toggles:
    if "no" + setting in sys.argv:
        enabled[setting] = False
    else:
        enabled[setting] = True

inputJSONs = processDir("input/data/minecraft/tags/items/")

for name, JSON in inputJSONs.items():
    tagName = "minecraft:" + name.split(".")[0]
    if tagName in TAGPOOL:
        processTag(JSON)

inputJSONs = processDir("input/data/minecraft/")
outputJSONs = copy.deepcopy(inputJSONs)

normBasePool = []
ingBasePool = []
positionStack = ["recipes"]
normPool, normBasePool = formItemPool(True, True, False)
ingPool, ingBasePool = formItemPool(True, False, True)

if enabled["reciperesult"] or enabled["recipeingredients"]:
    for name, JSON in inputJSONs["recipes"].items():
        positionStack.append(name)
        if enabled["reciperesult"] and (JSON["type"] == "minecraft:crafting_shaped" or JSON["type"] == "minecraft:crafting_shapeless"):
            print(name)
            processRecipeResult(positionStack)
        if enabled["recipeingredients"]:
            if JSON["type"] == "minecraft:crafting_shaped" :
                positionStack.append("key")
                dictFor(JSON["key"], positionStack, processRecipeIngredient)
                del positionStack[-1]
            if JSON["type"] == "minecraft:crafting_shapeless":
                positionStack.append("ingredients")
                listFor(JSON["ingredients"], positionStack, processRecipeIngredient)
                del positionStack[-1]
        if JSON["type"] == "minecraft:smelting" or JSON["type"] == "minecraft:stonecutting" or JSON["type"] == "minecraft:blasting" or JSON["type"] == "minecraft:campfire_cooking" or JSON["type"] == "minecraft:smoking":
            if enabled["reciperesult"]:
                processRecipeResult(positionStack)
            if enabled["recipeingredients"]:
                positionStack.append("ingredient")
                processRecipeIngredient(None, positionStack)
                del positionStack[-1]
        if JSON["type"] == "minecraft:smithing":
            if enabled["smithingbase"]:
                positionStack.append("base")
                processRecipeIngredient(None, positionStack)
                del positionStack[-1]
            if enabled["smithingaddition"]:
                positionStack.append("addition")
                processRecipeIngredient(None, positionStack)
                del positionStack[-1]
            if enabled["smithingresult"]:
                processRecipeResult(positionStack)
        del positionStack[-1]

positionStack = ["loot_tables"]
normPool = normPool + POTIONPOOL

if enabled["blockdrops"]:
    positionStack.append("blocks")
    processLootTables(inputJSONs["loot_tables"]["blocks"], positionStack)
    del positionStack[-1]

if enabled["chestcontents"]:
    positionStack.append("chests")
    processLootTables(inputJSONs["loot_tables"]["chests"], positionStack)
    positionStack.append("village")
    processLootTables(inputJSONs["loot_tables"]["chests"]["village"], positionStack)
    del positionStack[-1]
    del positionStack[-1]

if enabled["entitydrops"]:
    positionStack.append("entities")
    processLootTables(inputJSONs["loot_tables"]["entities"], positionStack)
    positionStack.append("sheep")
    processLootTables(inputJSONs["loot_tables"]["entities"]["sheep"], positionStack)
    del positionStack[-1]
    del positionStack[-1]

positionStack.append("gameplay")
if enabled["fishing"]:
    positionStack.append("fishing")
    processLootTables(inputJSONs["loot_tables"]["gameplay"]["fishing"], positionStack)
    del positionStack[-1]

if enabled["herogifts"]:
    positionStack.append("hero_of_the_village")
    processLootTables(inputJSONs["loot_tables"]["gameplay"]["hero_of_the_village"], positionStack)
    del positionStack[-1]

if enabled["piglinbarter"]:
    positionStack.append("piglin_bartering.json")
    processLootTable(inputJSONs["loot_tables"]["gameplay"]["piglin_bartering.json"], positionStack)
    del positionStack[-1]

if enabled["catgifts"]:
    positionStack.append("cat_morning_gift.json")
    processLootTable(inputJSONs["loot_tables"]["gameplay"]["cat_morning_gift.json"], positionStack)
    del positionStack[-1]

saveFolder(outputJSONs, "output/")

