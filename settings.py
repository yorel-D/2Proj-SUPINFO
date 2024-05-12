import pygame as game

CELL = 10
SCREEN_WIDTH = 128 * CELL
SCREEN_HEIGHT = 72 * CELL
DISPLAY = game.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
LOADING_SCREEN = game.image.load("Resources/LOADING.png").convert_alpha()
DISPLAY.blit(LOADING_SCREEN, (0, 0))
game.display.update()
BACKGROUND = game.image.load("Resources/bck2.png").convert_alpha()
CASTLE_IMAGE = game.image.load("Resources/castle_100.png").convert_alpha()
PLAYER_CASTLE_IMAGE = game.transform.scale(CASTLE_IMAGE, (20 * CELL, 20 * CELL))
PLAYER_CASTLE_IMAGE = game.transform.flip(PLAYER_CASTLE_IMAGE, True, False)
ENEMY_CASTLE_IMAGE = game.transform.scale(CASTLE_IMAGE, (20 * CELL, 20 * CELL))

PLAYER_HEAVY_PIRATE_WALKING = [game.image.load(f"Resources/Satyr_02_Walking_{i:03d}.png").convert_alpha() for i in range(18)]
PLAYER_HEAVY_PIRATE_WALKING = [game.transform.scale(image, (10 * CELL, 10 * CELL)) for image in PLAYER_HEAVY_PIRATE_WALKING]
PLAYER_HEAVY_PIRATE_ATTACKING = [game.image.load(f"Resources/Satyr_02_Attacking_{i:03d}.png").convert_alpha() for i in range(12)]
PLAYER_HEAVY_PIRATE_ATTACKING = [game.transform.scale(image, (10 * CELL, 10 * CELL)) for image in PLAYER_HEAVY_PIRATE_ATTACKING]
PLAYER_HEAVY_PIRATE_IDLE = [game.image.load(f"Resources/Satyr_02_Idle_{i:03d}.png").convert_alpha() for i in range(12)]
PLAYER_HEAVY_PIRATE_IDLE = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_HEAVY_PIRATE_IDLE]

PLAYER_LIGHT_PIRATE_WALKING = [game.image.load(f"Resources/Satyr_03_Walking_{i:03d}.png").convert_alpha() for i in range(18)]
PLAYER_LIGHT_PIRATE_WALKING = [game.transform.scale(image, (CELL * 10, CELL * 10)).convert_alpha() for image in PLAYER_LIGHT_PIRATE_WALKING]
PLAYER_LIGHT_PIRATE_ATTACKING = [game.image.load(f"Resources/Satyr_03_Attacking_{i:03d}.png").convert_alpha() for i in range(12)]
PLAYER_LIGHT_PIRATE_ATTACKING = [game.transform.scale(image, (CELL * 10, CELL * 10)).convert_alpha() for image in PLAYER_LIGHT_PIRATE_ATTACKING]
PLAYER_LIGHT_PIRATE_IDLE = [game.image.load(f"Resources/Satyr_03_Idle_{i:03d}.png").convert_alpha() for i in range(12)]
PLAYER_LIGHT_PIRATE_IDLE = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_LIGHT_PIRATE_IDLE]

PLAYER_RANGED_PIRATE_WALKING = [game.image.load(f"Resources/Satyr_01_Walking_{i:03d}.png").convert_alpha() for i in range(18)]
PLAYER_RANGED_PIRATE_WALKING = [game.transform.scale(image, (CELL * 10, CELL * 10)).convert_alpha() for image in PLAYER_RANGED_PIRATE_WALKING]
PLAYER_RANGED_PIRATE_ATTACKING = [game.image.load(f"Resources/Satyr_01_Attacking_{i:03d}.png").convert_alpha() for i in range(12)]
PLAYER_RANGED_PIRATE_ATTACKING = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_RANGED_PIRATE_ATTACKING]
PLAYER_RANGED_PIRATE_IDLE = [game.image.load(f"Resources/Satyr_01_Idle_{i:03d}.png").convert_alpha() for i in range(12)]
PLAYER_RANGED_PIRATE_IDLE = [game.transform.scale(image, (10 * CELL, 10 * CELL)) for image in PLAYER_RANGED_PIRATE_IDLE]

PLAYER_HERO_PIRATE_WALKING = [game.image.load(f"Resources/4_entity__WALK_00{i}.png").convert_alpha() for i in range(10)]
PLAYER_HERO_PIRATE_WALKING = [game.transform.scale(image, (CELL * 10, CELL * 10)).convert_alpha() for image in PLAYER_HERO_PIRATE_WALKING]
PLAYER_HERO_PIRATE_ATTACKING = [game.image.load(f"Resources/4_entity__ATTACK_00{i}.png").convert_alpha() for i in range(10)]
PLAYER_HERO_PIRATE_ATTACKING = [game.transform.scale(image, (CELL * 10, CELL * 10)).convert_alpha() for image in PLAYER_HERO_PIRATE_ATTACKING]
PLAYER_HERO_PIRATE_IDLE = [game.image.load(f"Resources/4_entity__IDLE_00{i}.png").convert_alpha() for i in range(10)]
PLAYER_HERO_PIRATE_IDLE = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_HERO_PIRATE_IDLE]


PLAYER_LIGHT_WARRIOR_WALIKNG = [game.image.load(f"Resources/0_Golem_Walking_{i:03d}.png").convert_alpha() for i in range(24)]
PLAYER_LIGHT_WARRIOR_WALIKNG = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_LIGHT_WARRIOR_WALIKNG]
PLAYER_LIGHT_WARRIOR_ATTACKING = [game.image.load(f"Resources/0_Golem_Slashing_{i:03d}.png").convert_alpha() for i in range(12)]
PLAYER_LIGHT_WARRIOR_ATTACKING = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_LIGHT_WARRIOR_ATTACKING]
PLAYER_LIGHT_WARRIOR_IDLE = [game.image.load(f"Resources/0_Golem_Idle_{i:03d}.png").convert_alpha() for i in range(18)]
PLAYER_LIGHT_WARRIOR_IDLE = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_LIGHT_WARRIOR_IDLE]

PLAYER_HEAVY_WARRIOR_WALIKNG = [game.image.load(f"Resources/1_Golem_Walking_{i:03d}.png").convert_alpha() for i in range(24)]
PLAYER_HEAVY_WARRIOR_WALIKNG = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_HEAVY_WARRIOR_WALIKNG]
PLAYER_HEAVY_WARRIOR_ATTACKING = [game.image.load(f"Resources/1_Golem_Slashing_{i:03d}.png").convert_alpha() for i in range(12)]
PLAYER_HEAVY_WARRIOR_ATTACKING = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_HEAVY_WARRIOR_ATTACKING]
PLAYER_HEAVY_WARRIOR_IDLE = [game.image.load(f"Resources/1_Golem_Idle_{i:03d}.png").convert_alpha() for i in range(18)]
PLAYER_HEAVY_WARRIOR_IDLE = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_HEAVY_WARRIOR_IDLE]

PLAYER_RANGED_WARRIOR_WALIKNG = [game.image.load(f"Resources/2_Golem_Walking_{i:03d}.png").convert_alpha() for i in range(24)]
PLAYER_RANGED_WARRIOR_WALIKNG = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_RANGED_WARRIOR_WALIKNG]
PLAYER_RANGED_WARRIOR_ATTACKING = [game.image.load(f"Resources/2_Golem_Slashing_{i:03d}.png").convert_alpha() for i in range(12)]
PLAYER_RANGED_WARRIOR_ATTACKING = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_RANGED_WARRIOR_ATTACKING]
PLAYER_RANGED_WARRIOR_IDLE = [game.image.load(f"Resources/2_Golem_Idle_{i:03d}.png").convert_alpha() for i in range(18)]
PLAYER_RANGED_WARRIOR_IDLE = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_RANGED_WARRIOR_IDLE]


PLAYER_RANGED_ELF_WALKING = [game.image.load(f"Resources/Fairy_01__WALK_00{i}.png").convert_alpha() for i in range(10)]
PLAYER_RANGED_ELF_WALKING = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_RANGED_ELF_WALKING]
PLAYER_RANGED_ELF_ATTACKING = [game.image.load(f"Resources/Fairy_01__ATTACK_00{i}.png").convert_alpha() for i in range(10)]
PLAYER_RANGED_ELF_ATTACKING = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_RANGED_ELF_ATTACKING]
PLAYER_RANGED_ELF_IDLE = [game.image.load(f"Resources/Fairy_01__IDLE_00{i}.png").convert_alpha() for i in range(10)]
PLAYER_RANGED_ELF_IDLE = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_RANGED_ELF_IDLE]

PLAYER_HEAVY_ELF_WALKING = [game.image.load(f"Resources/Fairy_02__WALK_00{i}.png").convert_alpha() for i in range(10)]
PLAYER_HEAVY_ELF_WALKING = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_HEAVY_ELF_WALKING]
PLAYER_HEAVY_ELF_ATTACKING = [game.image.load(f"Resources/Fairy_02__ATTACK_00{i}.png").convert_alpha() for i in range(10)]
PLAYER_HEAVY_ELF_ATTACKING = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_HEAVY_ELF_ATTACKING]
PLAYER_HEAVY_ELF_IDLE = [game.image.load(f"Resources/Fairy_02__IDLE_00{i}.png").convert_alpha() for i in range(10)]
PLAYER_HEAVY_ELF_IDLE = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_HEAVY_ELF_IDLE]

PLAYER_LIGHT_ELF_WALKING = [game.image.load(f"Resources/Fairy_03__WALK_00{i}.png").convert_alpha() for i in range(10)]
PLAYER_LIGHT_ELF_WALKING = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_LIGHT_ELF_WALKING]
PLAYER_LIGHT_ELF_ATTACKING = [game.image.load(f"Resources/Fairy_03__ATTACK_00{i}.png").convert_alpha() for i in range(10)]
PLAYER_LIGHT_ELF_ATTACKING = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_LIGHT_ELF_ATTACKING]
PLAYER_LIGHT_ELF_IDLE = [game.image.load(f"Resources/Fairy_03__IDLE_00{i}.png").convert_alpha() for i in range(10)]
PLAYER_LIGHT_ELF_IDLE = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_LIGHT_ELF_IDLE]


PLAYER_RANGED_PIRATE_BULLET = game.image.load("Resources/shot.png")
PLAYER_RANGED_PIRATE_BULLET = game.transform.scale(PLAYER_RANGED_PIRATE_BULLET, (1 * CELL, 0.5 * CELL))


ENEMY_LIGHT_PIRATE_WALKING = [game.transform.flip(image, True, False) for image in PLAYER_LIGHT_PIRATE_WALKING]
ENEMY_LIGHT_PIRATE_ATTACKING = [game.transform.flip(image, True, False) for image in PLAYER_LIGHT_PIRATE_ATTACKING]
ENEMY_LIGHT_PIRATE_IDLE = [game.transform.flip(image, True, False) for image in PLAYER_LIGHT_PIRATE_IDLE]

ENEMY_HEAVY_PIRATE_WALKING = [game.transform.flip(image, True, False) for image in PLAYER_HEAVY_PIRATE_WALKING]
ENEMY_HEAVY_PIRATE_ATTACKING = [game.transform.flip(image, True, False) for image in PLAYER_HEAVY_PIRATE_ATTACKING]
ENEMY_HEAVY_PIRATE_IDLE = [game.transform.flip(image, True, False) for image in PLAYER_HEAVY_PIRATE_IDLE]

ENEMY_HERO_PIRATE_WALKING = [game.transform.flip(image, True, False) for image in PLAYER_HERO_PIRATE_WALKING]
ENEMY_HERO_PIRATE_ATTACKING = [game.transform.flip(image, True, False) for image in PLAYER_HERO_PIRATE_ATTACKING]
ENEMY_HERO_PIRATE_IDLE = [game.transform.flip(image, True, False) for image in PLAYER_HERO_PIRATE_IDLE]

ENEMY_RANGED_PIRATE_WALKING = [game.transform.flip(image, True, False) for image in PLAYER_RANGED_PIRATE_WALKING]
ENEMY_RANGED_PIRATE_ATTACKING = [game.transform.flip(image, True, False) for image in PLAYER_RANGED_PIRATE_ATTACKING]
ENEMY_RANGED_PIRATE_IDLE = [game.transform.flip(image, True, False) for image in PLAYER_RANGED_PIRATE_IDLE]

ENEMY_LIGHT_WARRIOR_WALKING = [game.transform.flip(image, True, False) for image in PLAYER_LIGHT_WARRIOR_WALIKNG]
ENEMY_LIGHT_WARRIOR_ATTACKING = [game.transform.flip(image, True, False) for image in PLAYER_LIGHT_WARRIOR_ATTACKING]
ENEMY_LIGHT_WARRIOR_IDLE = [game.transform.flip(image, True, False) for image in PLAYER_LIGHT_WARRIOR_IDLE]

ENEMY_HEAVY_WARRIOR_WALKING = [game.transform.flip(image, True, False) for image in PLAYER_HEAVY_WARRIOR_WALIKNG]
ENEMY_HEAVY_WARRIOR_ATTACKING = [game.transform.flip(image, True, False) for image in PLAYER_HEAVY_WARRIOR_ATTACKING]
ENEMY_HEAVY_WARRIOR_IDLE= [game.transform.flip(image, True, False) for image in PLAYER_HEAVY_WARRIOR_IDLE]

ENEMY_RANGED_WARRIOR_WALKING = [game.transform.flip(image, True, False) for image in PLAYER_RANGED_WARRIOR_WALIKNG]
ENEMY_RANGED_WARRIOR_ATTACKING = [game.transform.flip(image, True, False) for image in PLAYER_RANGED_WARRIOR_ATTACKING]
ENEMY_RANGED_WARRIOR_IDLE = [game.transform.flip(image, True, False) for image in PLAYER_RANGED_WARRIOR_IDLE]

ENEMY_LIGHT_ELF_WALKING = [game.transform.flip(image, True, False) for image in PLAYER_LIGHT_ELF_WALKING]
ENEMY_LIGHT_ELF_ATTACKING = [game.transform.flip(image, True, False) for image in PLAYER_LIGHT_ELF_ATTACKING]
ENEMY_LIGHT_ELF_IDLE = [game.transform.flip(image, True, False) for image in PLAYER_LIGHT_ELF_IDLE]

ENEMY_HEAVY_ELF_WALKING = [game.transform.flip(image, True, False) for image in PLAYER_HEAVY_ELF_WALKING]
ENEMY_HEAVY_ELF_ATTACKING = [game.transform.flip(image, True, False) for image in PLAYER_HEAVY_ELF_ATTACKING]
ENEMY_HEAVY_ELF_IDLE = [game.transform.flip(image, True, False) for image in PLAYER_HEAVY_ELF_IDLE]

ENEMY_RANGED_ELF_WALKING = [game.transform.flip(image, True, False) for image in PLAYER_RANGED_ELF_WALKING]
ENEMY_RANGED_ELF_ATTACKING = [game.transform.flip(image, True, False) for image in PLAYER_RANGED_ELF_ATTACKING]
ENEMY_RANGED_ELF_IDLE = [game.transform.flip(image, True, False) for image in PLAYER_RANGED_ELF_IDLE]

LIGHT_PIRATE_ICON = game.image.load("Resources/light_Satyr_icon.png").convert_alpha()
LIGHT_PIRATE_ICON = game.transform.scale(LIGHT_PIRATE_ICON, (7 * CELL, 7 * CELL))
RANGED_PIRATE_ICON = game.image.load("Resources/ranged_Satyr_icon.png").convert_alpha()
RANGED_PIRATE_ICON = game.transform.scale(RANGED_PIRATE_ICON, (7 * CELL, 7 * CELL))
HEAVY_PIRATE_ICON = game.image.load("Resources/heavy_Satyr_icon.png").convert_alpha()
HEAVY_PIRATE_ICON = game.transform.scale(HEAVY_PIRATE_ICON, (7 * CELL, 7 * CELL))
HERO_PIRATE_ICON = game.image.load("Resources/hero_pirate_icon.png").convert_alpha()
HERO_PIRATE_ICON = game.transform.scale(HERO_PIRATE_ICON, (7 * CELL, 7 * CELL))
LIGHT_WARRIOR_ICON = game.image.load("Resources/light_golem_icon.png").convert_alpha()
LIGHT_WARRIOR_ICON = game.transform.scale(LIGHT_WARRIOR_ICON, (7 * CELL, 7 * CELL))
HEAVY_WARRIOR_ICON = game.image.load("Resources/heavy_golem_icon.png").convert_alpha()
HEAVY_WARRIOR_ICON = game.transform.scale(HEAVY_WARRIOR_ICON, (7 * CELL, 7 * CELL))
RANGED_WARRIOR_ICON = game.image.load("Resources/ranged_golem_icon.png").convert_alpha()
RANGED_WARRIOR_ICON = game.transform.scale(RANGED_WARRIOR_ICON, (7 * CELL, 7 * CELL))
LIGHT_ELF_ICON = game.image.load("Resources/ranged_fairy_icon.png").convert_alpha()
LIGHT_ELF_ICON = game.transform.scale(LIGHT_ELF_ICON, (7 * CELL, 7 * CELL))
HEAVY_ELF_ICON = game.image.load("Resources/heavy_fairy_icon.png").convert_alpha()
HEAVY_ELF_ICON = game.transform.scale(HEAVY_ELF_ICON, (7 * CELL, 7 * CELL))
RANGED_ELF_ICON = game.image.load("Resources/light_fairy_icon.png").convert_alpha()
RANGED_ELF_ICON = game.transform.scale(RANGED_ELF_ICON, (7 * CELL, 7 * CELL))
PIRATE_TURRET_ICON = game.image.load("Resources/pirate_turret_icon.png").convert_alpha()
PIRATE_TURRET_ICON = game.transform.scale(PIRATE_TURRET_ICON, (7 * CELL, 7 * CELL))
WARRIOR_TURRET_ICON = game.image.load("Resources/warrior_turret_icon.png").convert_alpha()
WARRIOR_TURRET_ICON = game.transform.scale(WARRIOR_TURRET_ICON, (7 * CELL, 7 * CELL))
TURRET_UPGRADE_ICON = game.image.load("Resources/turret_upgrade_icon.png").convert_alpha()
TURRET_UPGRADE_ICON = game.transform.scale(TURRET_UPGRADE_ICON, (7 * CELL, 7 * CELL))
ELF_TURRET_ICON = game.image.load("Resources/elf_turret_icon.png").convert_alpha()
ELF_TURRET_ICON = game.transform.scale(ELF_TURRET_ICON, (7 * CELL, 7 * CELL))
PLAYER_PIRATE_TURRET = game.image.load("Resources/pirate_turret.png").convert_alpha()
PLAYER_PIRATE_TURRET = game.transform.scale(PLAYER_PIRATE_TURRET, (4 * CELL, 4 * CELL))
ENEMY_PIRATE_TURRET = game.transform.flip(PLAYER_PIRATE_TURRET, True, False)
PLAYER_WARRIOR_TURRET = game.image.load("Resources/warrior_turret.png").convert_alpha()
PLAYER_WARRIOR_TURRET = game.transform.scale(PLAYER_WARRIOR_TURRET, (4 * CELL, 4 * CELL))
ENEMY_WARRIOR_TURRET = game.transform.flip(PLAYER_WARRIOR_TURRET, True, False)
PLAYER_ELF_TURRET = game.image.load("Resources/elf_turret.png").convert_alpha()
PLAYER_ELF_TURRET = game.transform.scale(PLAYER_ELF_TURRET, (4 * CELL, 4 * CELL))
ENEMY_ELF_TURRET = game.transform.flip(PLAYER_ELF_TURRET, True, False)
SELL_BUTTON = game.image.load("Resources/dollar-symbol.png").convert_alpha()
REPAIR_BUTTON = game.image.load("Resources/tool.png").convert_alpha()
PIRATE_CANNONBALL= game.image.load("Resources/pirate_cannonball.png").convert_alpha()
PIRATE_CANNONBALL = game.transform.scale(PIRATE_CANNONBALL, (1 * CELL, 1 * CELL))
WARRIOR_CANNONBALL = game.image.load("Resources/warrior_cannonball.png").convert_alpha()
WARRIOR_CANNONBALL =  game.transform.scale(WARRIOR_CANNONBALL, (1 * CELL, 1 * CELL))
ELF_CANNONBALL = game.image.load("Resources/elf_cannonball.png").convert_alpha()
ELF_CANNONBALL = game.transform.scale(ELF_CANNONBALL, (1 * CELL, 1 * CELL))
UPGRADE_BUTTON = game.image.load("Resources/upgrade_button.png").convert_alpha()
GAME_OVER = game.image.load("Resources/game_over.png").convert_alpha()
GAME_WON = game.image.load("Resources/game_won.png").convert_alpha()