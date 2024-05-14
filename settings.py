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

PLAYER_LIGHT_SATYR_WALKING = [game.image.load(f"Resources/Satyr_03_Walking_{i:03d}.png").convert_alpha() for i in range(18)]
PLAYER_LIGHT_SATYR_WALKING = [game.transform.scale(image, (CELL * 10, CELL * 10)).convert_alpha() for image in PLAYER_LIGHT_SATYR_WALKING]
PLAYER_LIGHT_SATYR_ATTACKING = [game.image.load(f"Resources/Satyr_03_Attacking_{i:03d}.png").convert_alpha() for i in range(12)]
PLAYER_LIGHT_SATYR_ATTACKING = [game.transform.scale(image, (CELL * 10, CELL * 10)).convert_alpha() for image in PLAYER_LIGHT_SATYR_ATTACKING]
PLAYER_LIGHT_SATYR_IDLE = [game.image.load(f"Resources/Satyr_03_Idle_{i:03d}.png").convert_alpha() for i in range(12)]
PLAYER_LIGHT_SATYR_IDLE = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_LIGHT_SATYR_IDLE]

PLAYER_RANGED_SATYR_WALKING = [game.image.load(f"Resources/Satyr_01_Walking_{i:03d}.png").convert_alpha() for i in range(18)]
PLAYER_RANGED_SATYR_WALKING = [game.transform.scale(image, (CELL * 10, CELL * 10)).convert_alpha() for image in PLAYER_RANGED_SATYR_WALKING]
PLAYER_RANGED_SATYR_ATTACKING = [game.image.load(f"Resources/Satyr_01_Attacking_{i:03d}.png").convert_alpha() for i in range(12)]
PLAYER_RANGED_SATYR_ATTACKING = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_RANGED_SATYR_ATTACKING]
PLAYER_RANGED_SATYR_IDLE = [game.image.load(f"Resources/Satyr_01_Idle_{i:03d}.png").convert_alpha() for i in range(12)]
PLAYER_RANGED_SATYR_IDLE = [game.transform.scale(image, (10 * CELL, 10 * CELL)) for image in PLAYER_RANGED_SATYR_IDLE]

PLAYER_HEAVY_SATYR_WALKING = [game.image.load(f"Resources/Satyr_02_Walking_{i:03d}.png").convert_alpha() for i in range(18)]
PLAYER_HEAVY_SATYR_WALKING = [game.transform.scale(image, (10 * CELL, 10 * CELL)) for image in PLAYER_HEAVY_SATYR_WALKING]
PLAYER_HEAVY_SATYR_ATTACKING = [game.image.load(f"Resources/Satyr_02_Attacking_{i:03d}.png").convert_alpha() for i in range(12)]
PLAYER_HEAVY_SATYR_ATTACKING = [game.transform.scale(image, (10 * CELL, 10 * CELL)) for image in PLAYER_HEAVY_SATYR_ATTACKING]
PLAYER_HEAVY_SATYR_IDLE = [game.image.load(f"Resources/Satyr_02_Idle_{i:03d}.png").convert_alpha() for i in range(12)]
PLAYER_HEAVY_SATYR_IDLE = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_HEAVY_SATYR_IDLE]

PLAYER_HERO_SATYR_WALKING = [game.image.load(f"Resources/4_entity__WALK_00{i}.png").convert_alpha() for i in range(10)]
PLAYER_HERO_SATYR_WALKING = [game.transform.scale(image, (CELL * 10, CELL * 10)).convert_alpha() for image in PLAYER_HERO_SATYR_WALKING]
PLAYER_HERO_SATYR_ATTACKING = [game.image.load(f"Resources/4_entity__ATTACK_00{i}.png").convert_alpha() for i in range(10)]
PLAYER_HERO_SATYR_ATTACKING = [game.transform.scale(image, (CELL * 10, CELL * 10)).convert_alpha() for image in PLAYER_HERO_SATYR_ATTACKING]
PLAYER_HERO_SATYR_IDLE = [game.image.load(f"Resources/4_entity__IDLE_00{i}.png").convert_alpha() for i in range(10)]
PLAYER_HERO_SATYR_IDLE = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_HERO_SATYR_IDLE]



PLAYER_LIGHT_GOLEM_WALIKNG = [game.image.load(f"Resources/0_Golem_Walking_{i:03d}.png").convert_alpha() for i in range(24)]
PLAYER_LIGHT_GOLEM_WALIKNG = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_LIGHT_GOLEM_WALIKNG]
PLAYER_LIGHT_GOLEM_ATTACKING = [game.image.load(f"Resources/0_Golem_Slashing_{i:03d}.png").convert_alpha() for i in range(12)]
PLAYER_LIGHT_GOLEM_ATTACKING = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_LIGHT_GOLEM_ATTACKING]
PLAYER_LIGHT_GOLEM_IDLE = [game.image.load(f"Resources/0_Golem_Idle_{i:03d}.png").convert_alpha() for i in range(18)]
PLAYER_LIGHT_GOLEM_IDLE = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_LIGHT_GOLEM_IDLE]

PLAYER_RANGED_GOLEM_WALIKNG = [game.image.load(f"Resources/2_Golem_Walking_{i:03d}.png").convert_alpha() for i in range(24)]
PLAYER_RANGED_GOLEM_WALIKNG = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_RANGED_GOLEM_WALIKNG]
PLAYER_RANGED_GOLEM_ATTACKING = [game.image.load(f"Resources/2_Golem_Slashing_{i:03d}.png").convert_alpha() for i in range(12)]
PLAYER_RANGED_GOLEM_ATTACKING = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_RANGED_GOLEM_ATTACKING]
PLAYER_RANGED_GOLEM_IDLE = [game.image.load(f"Resources/2_Golem_Idle_{i:03d}.png").convert_alpha() for i in range(18)]
PLAYER_RANGED_GOLEM_IDLE = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_RANGED_GOLEM_IDLE]

PLAYER_HEAVY_GOLEM_WALIKNG = [game.image.load(f"Resources/1_Golem_Walking_{i:03d}.png").convert_alpha() for i in range(24)]
PLAYER_HEAVY_GOLEM_WALIKNG = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_HEAVY_GOLEM_WALIKNG]
PLAYER_HEAVY_GOLEM_ATTACKING = [game.image.load(f"Resources/1_Golem_Slashing_{i:03d}.png").convert_alpha() for i in range(12)]
PLAYER_HEAVY_GOLEM_ATTACKING = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_HEAVY_GOLEM_ATTACKING]
PLAYER_HEAVY_GOLEM_IDLE = [game.image.load(f"Resources/1_Golem_Idle_{i:03d}.png").convert_alpha() for i in range(18)]
PLAYER_HEAVY_GOLEM_IDLE = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_HEAVY_GOLEM_IDLE]

PLAYER_HERO_GOLEM_WALIKNG = [game.image.load(f"Resources/Knight_01__WALK_{i:03d}.png").convert_alpha() for i in range(10)]
PLAYER_HERO_GOLEM_WALIKNG = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_HERO_GOLEM_WALIKNG]
PLAYER_HERO_GOLEM_ATTACKING = [game.image.load(f"Resources/Knight_01__ATTACK_{i:03d}.png").convert_alpha() for i in range(10)]
PLAYER_HERO_GOLEM_ATTACKING = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_HERO_GOLEM_ATTACKING]
PLAYER_HERO_GOLEM_IDLE = [game.image.load(f"Resources/Knight_01__IDLE_{i:03d}.png").convert_alpha() for i in range(10)]
PLAYER_HERO_GOLEM_IDLE = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_HERO_GOLEM_IDLE]



PLAYER_LIGHT_ELF_WALKING = [game.image.load(f"Resources/Fairy_03__WALK_00{i}.png").convert_alpha() for i in range(10)]
PLAYER_LIGHT_ELF_WALKING = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_LIGHT_ELF_WALKING]
PLAYER_LIGHT_ELF_ATTACKING = [game.image.load(f"Resources/Fairy_03__ATTACK_00{i}.png").convert_alpha() for i in range(10)]
PLAYER_LIGHT_ELF_ATTACKING = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_LIGHT_ELF_ATTACKING]
PLAYER_LIGHT_ELF_IDLE = [game.image.load(f"Resources/Fairy_03__IDLE_00{i}.png").convert_alpha() for i in range(10)]
PLAYER_LIGHT_ELF_IDLE = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_LIGHT_ELF_IDLE]

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

PLAYER_HERO_ELF_WALKING = [game.image.load(f"Resources/Knight_03__WALK_00{i}.png").convert_alpha() for i in range(10)]
PLAYER_HERO_ELF_WALKING = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_HERO_ELF_WALKING]
PLAYER_HERO_ELF_ATTACKING = [game.image.load(f"Resources/Knight_03__ATTACK_00{i}.png").convert_alpha() for i in range(10)]
PLAYER_HERO_ELF_ATTACKING = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_HERO_ELF_ATTACKING]
PLAYER_HERO_ELF_IDLE = [game.image.load(f"Resources/Knight_03__IDLE_00{i}.png").convert_alpha() for i in range(10)]
PLAYER_HERO_ELF_IDLE = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_HERO_ELF_IDLE]



PLAYER_LIGHT_ANGEL_WALKING = [game.image.load(f"Resources/0_Fallen_Angels_Walking_{i:03d}.png").convert_alpha() for i in range(24)]
PLAYER_LIGHT_ANGEL_WALKING = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_LIGHT_ANGEL_WALKING]
PLAYER_LIGHT_ANGEL_ATTACKING = [game.image.load(f"Resources/0_Fallen_Angels_Slashing_{i:03d}.png").convert_alpha() for i in range(12)]
PLAYER_LIGHT_ANGEL_ATTACKING = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_LIGHT_ANGEL_ATTACKING]
PLAYER_LIGHT_ANGEL_IDLE = [game.image.load(f"Resources/0_Fallen_Angels_Idle_{i:03d}.png").convert_alpha() for i in range(18)]
PLAYER_LIGHT_ANGEL_IDLE = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_LIGHT_ANGEL_IDLE]

PLAYER_HEAVY_ANGEL_WALKING = [game.image.load(f"Resources/1_Fallen_Angels_Walking_{i:03d}.png").convert_alpha() for i in range(24)]
PLAYER_HEAVY_ANGEL_WALKING = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_HEAVY_ANGEL_WALKING]
PLAYER_HEAVY_ANGEL_ATTACKING = [game.image.load(f"Resources/1_Fallen_Angels_Slashing_{i:03d}.png").convert_alpha() for i in range(12)]
PLAYER_HEAVY_ANGEL_ATTACKING = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_HEAVY_ANGEL_ATTACKING]
PLAYER_HEAVY_ANGEL_IDLE = [game.image.load(f"Resources/1_Fallen_Angels_Idle_{i:03d}.png").convert_alpha() for i in range(18)]
PLAYER_HEAVY_ANGEL_IDLE = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_HEAVY_ANGEL_IDLE]

PLAYER_RANGED_ANGEL_WALKING = [game.image.load(f"Resources/2_Fallen_Angels_Walking_{i:03d}.png").convert_alpha() for i in range(24)]
PLAYER_RANGED_ANGEL_WALKING = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_RANGED_ANGEL_WALKING]
PLAYER_RANGED_ANGEL_ATTACKING = [game.image.load(f"Resources/2_Fallen_Angels_Slashing_{i:03d}.png").convert_alpha() for i in range(12)]
PLAYER_RANGED_ANGEL_ATTACKING = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_RANGED_ANGEL_ATTACKING]
PLAYER_RANGED_ANGEL_IDLE = [game.image.load(f"Resources/2_Fallen_Angels_Idle_{i:03d}.png").convert_alpha() for i in range(18)]
PLAYER_RANGED_ANGEL_IDLE = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_RANGED_ANGEL_IDLE]

PLAYER_HERO_ANGEL_WALKING = [game.image.load(f"Resources/0_Reaper_Man_Walking_{i:03d}.png").convert_alpha() for i in range(24)]
PLAYER_HERO_ANGEL_WALKING = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_HERO_ANGEL_WALKING]
PLAYER_HERO_ANGEL_ATTACKING = [game.image.load(f"Resources/0_Reaper_Man_Slashing_{i:03d}.png").convert_alpha() for i in range(12)]
PLAYER_HERO_ANGEL_ATTACKING = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_HERO_ANGEL_ATTACKING]
PLAYER_HERO_ANGEL_IDLE = [game.image.load(f"Resources/0_Reaper_Man_Idle_{i:03d}.png").convert_alpha() for i in range(18)]
PLAYER_HERO_ANGEL_IDLE = [game.transform.scale(image, (CELL * 10, CELL * 10)) for image in PLAYER_HERO_ANGEL_IDLE]


PLAYER_RANGED_SATYR_BULLET = game.image.load("Resources/shot.png")
PLAYER_RANGED_SATYR_BULLET = game.transform.scale(PLAYER_RANGED_SATYR_BULLET, (1 * CELL, 0.5 * CELL))


ENEMY_LIGHT_SATYR_WALKING = [game.transform.flip(image, True, False) for image in PLAYER_LIGHT_SATYR_WALKING]
ENEMY_LIGHT_SATYR_ATTACKING = [game.transform.flip(image, True, False) for image in PLAYER_LIGHT_SATYR_ATTACKING]
ENEMY_LIGHT_SATYR_IDLE = [game.transform.flip(image, True, False) for image in PLAYER_LIGHT_SATYR_IDLE]

ENEMY_HEAVY_SATYR_WALKING = [game.transform.flip(image, True, False) for image in PLAYER_HEAVY_SATYR_WALKING]
ENEMY_HEAVY_SATYR_ATTACKING = [game.transform.flip(image, True, False) for image in PLAYER_HEAVY_SATYR_ATTACKING]
ENEMY_HEAVY_SATYR_IDLE = [game.transform.flip(image, True, False) for image in PLAYER_HEAVY_SATYR_IDLE]

ENEMY_HERO_SATYR_WALKING = [game.transform.flip(image, True, False) for image in PLAYER_HERO_SATYR_WALKING]
ENEMY_HERO_SATYR_ATTACKING = [game.transform.flip(image, True, False) for image in PLAYER_HERO_SATYR_ATTACKING]
ENEMY_HERO_SATYR_IDLE = [game.transform.flip(image, True, False) for image in PLAYER_HERO_SATYR_IDLE]

ENEMY_RANGED_SATYR_WALKING = [game.transform.flip(image, True, False) for image in PLAYER_RANGED_SATYR_WALKING]
ENEMY_RANGED_SATYR_ATTACKING = [game.transform.flip(image, True, False) for image in PLAYER_RANGED_SATYR_ATTACKING]
ENEMY_RANGED_SATYR_IDLE = [game.transform.flip(image, True, False) for image in PLAYER_RANGED_SATYR_IDLE]

ENEMY_LIGHT_GOLEM_WALKING = [game.transform.flip(image, True, False) for image in PLAYER_LIGHT_GOLEM_WALIKNG]
ENEMY_LIGHT_GOLEM_ATTACKING = [game.transform.flip(image, True, False) for image in PLAYER_LIGHT_GOLEM_ATTACKING]
ENEMY_LIGHT_GOLEM_IDLE = [game.transform.flip(image, True, False) for image in PLAYER_LIGHT_GOLEM_IDLE]

ENEMY_HEAVY_GOLEM_WALKING = [game.transform.flip(image, True, False) for image in PLAYER_HEAVY_GOLEM_WALIKNG]
ENEMY_HEAVY_GOLEM_ATTACKING = [game.transform.flip(image, True, False) for image in PLAYER_HEAVY_GOLEM_ATTACKING]
ENEMY_HEAVY_GOLEM_IDLE= [game.transform.flip(image, True, False) for image in PLAYER_HEAVY_GOLEM_IDLE]

ENEMY_RANGED_GOLEM_WALKING = [game.transform.flip(image, True, False) for image in PLAYER_RANGED_GOLEM_WALIKNG]
ENEMY_RANGED_GOLEM_ATTACKING = [game.transform.flip(image, True, False) for image in PLAYER_RANGED_GOLEM_ATTACKING]
ENEMY_RANGED_GOLEM_IDLE = [game.transform.flip(image, True, False) for image in PLAYER_RANGED_GOLEM_IDLE]

ENEMY_HERO_GOLEM_WALKING = [game.transform.flip(image, True, False) for image in PLAYER_HERO_GOLEM_WALIKNG]
ENEMY_HERO_GOLEM_ATTACKING = [game.transform.flip(image, True, False) for image in PLAYER_HERO_GOLEM_ATTACKING]
ENEMY_HERO_GOLEM_IDLE = [game.transform.flip(image, True, False) for image in PLAYER_HERO_GOLEM_IDLE]

ENEMY_LIGHT_ELF_WALKING = [game.transform.flip(image, True, False) for image in PLAYER_LIGHT_ELF_WALKING]
ENEMY_LIGHT_ELF_ATTACKING = [game.transform.flip(image, True, False) for image in PLAYER_LIGHT_ELF_ATTACKING]
ENEMY_LIGHT_ELF_IDLE = [game.transform.flip(image, True, False) for image in PLAYER_LIGHT_ELF_IDLE]

ENEMY_HEAVY_ELF_WALKING = [game.transform.flip(image, True, False) for image in PLAYER_HEAVY_ELF_WALKING]
ENEMY_HEAVY_ELF_ATTACKING = [game.transform.flip(image, True, False) for image in PLAYER_HEAVY_ELF_ATTACKING]
ENEMY_HEAVY_ELF_IDLE = [game.transform.flip(image, True, False) for image in PLAYER_HEAVY_ELF_IDLE]

ENEMY_RANGED_ELF_WALKING = [game.transform.flip(image, True, False) for image in PLAYER_RANGED_ELF_WALKING]
ENEMY_RANGED_ELF_ATTACKING = [game.transform.flip(image, True, False) for image in PLAYER_RANGED_ELF_ATTACKING]
ENEMY_RANGED_ELF_IDLE = [game.transform.flip(image, True, False) for image in PLAYER_RANGED_ELF_IDLE]

LIGHT_SATYR_ICON = game.image.load("Resources/light_Satyr_icon.png").convert_alpha()
LIGHT_SATYR_ICON = game.transform.scale(LIGHT_SATYR_ICON, (7 * CELL, 7 * CELL))
RANGED_SATYR_ICON = game.image.load("Resources/ranged_Satyr_icon.png").convert_alpha()
RANGED_SATYR_ICON = game.transform.scale(RANGED_SATYR_ICON, (7 * CELL, 7 * CELL))
HEAVY_SATYR_ICON = game.image.load("Resources/heavy_Satyr_icon.png").convert_alpha()
HEAVY_SATYR_ICON = game.transform.scale(HEAVY_SATYR_ICON, (7 * CELL, 7 * CELL))
HERO_SATYR_ICON = game.image.load("Resources/hero_satyr_icon.png").convert_alpha()
HERO_SATYR_ICON = game.transform.scale(HERO_SATYR_ICON, (7 * CELL, 7 * CELL))
LIGHT_GOLEM_ICON = game.image.load("Resources/light_golem_icon.png").convert_alpha()
LIGHT_GOLEM_ICON = game.transform.scale(LIGHT_GOLEM_ICON, (7 * CELL, 7 * CELL))
HEAVY_GOLEM_ICON = game.image.load("Resources/heavy_golem_icon.png").convert_alpha()
HEAVY_GOLEM_ICON = game.transform.scale(HEAVY_GOLEM_ICON, (7 * CELL, 7 * CELL))
RANGED_GOLEM_ICON = game.image.load("Resources/ranged_golem_icon.png").convert_alpha()
RANGED_GOLEM_ICON = game.transform.scale(RANGED_GOLEM_ICON, (7 * CELL, 7 * CELL))
HERO_GOLEM_ICON = game.image.load("Resources/hero_golem_icon.png").convert_alpha()
HERO_GOLEM_ICON = game.transform.scale(HERO_GOLEM_ICON, (7 * CELL, 7 * CELL))
LIGHT_ELF_ICON = game.image.load("Resources/ranged_fairy_icon.png").convert_alpha()
LIGHT_ELF_ICON = game.transform.scale(LIGHT_ELF_ICON, (7 * CELL, 7 * CELL))
HEAVY_ELF_ICON = game.image.load("Resources/heavy_fairy_icon.png").convert_alpha()
HEAVY_ELF_ICON = game.transform.scale(HEAVY_ELF_ICON, (7 * CELL, 7 * CELL))
RANGED_ELF_ICON = game.image.load("Resources/light_fairy_icon.png").convert_alpha()
RANGED_ELF_ICON = game.transform.scale(RANGED_ELF_ICON, (7 * CELL, 7 * CELL))
HERO_ELF_ICON = game.image.load("Resources/hero_elf_icon.png").convert_alpha()
HERO_ELF_ICON = game.transform.scale(HERO_ELF_ICON, (7 * CELL, 7 * CELL))
LIGHT_ANGEL_ICON = game.image.load("Resources/light_angel_icon.png").convert_alpha()
LIGHT_ANGEL_ICON = game.transform.scale(LIGHT_ANGEL_ICON, (7 * CELL, 7 * CELL))
RANGED_ANGEL_ICON = game.image.load("Resources/heavy_angel_icon.png").convert_alpha()
RANGED_ANGEL_ICON = game.transform.scale(RANGED_ANGEL_ICON, (7 * CELL, 7 * CELL))
HEAVY_ANGEL_ICON = game.image.load("Resources/ranged_angel_icon.png").convert_alpha()
HEAVY_ANGEL_ICON = game.transform.scale(HEAVY_ANGEL_ICON, (7 * CELL, 7 * CELL))
HERO_ANGEL_ICON = game.image.load("Resources/hero_angel_icon.png").convert_alpha()
HERO_ANGEL_ICON = game.transform.scale(HERO_ANGEL_ICON, (7 * CELL, 7 * CELL))


SATYR_TURRET_ICON = game.image.load("Resources/satyr_turret_icon.png").convert_alpha()
SATYR_TURRET_ICON = game.transform.scale(SATYR_TURRET_ICON, (7 * CELL, 7 * CELL))
GOLEM_TURRET_ICON = game.image.load("Resources/golem_turret_icon.png").convert_alpha()
GOLEM_TURRET_ICON = game.transform.scale(GOLEM_TURRET_ICON, (7 * CELL, 7 * CELL))
TURRET_UPGRADE_ICON = game.image.load("Resources/turret_upgrade_icon.png").convert_alpha()
TURRET_UPGRADE_ICON = game.transform.scale(TURRET_UPGRADE_ICON, (7 * CELL, 7 * CELL))
ELF_TURRET_ICON = game.image.load("Resources/elf_turret_icon.png").convert_alpha()
ELF_TURRET_ICON = game.transform.scale(ELF_TURRET_ICON, (7 * CELL, 7 * CELL))
PLAYER_SATYR_TURRET = game.image.load("Resources/satyr_turret.png").convert_alpha()
PLAYER_SATYR_TURRET = game.transform.scale(PLAYER_SATYR_TURRET, (4 * CELL, 4 * CELL))
ENEMY_SATYR_TURRET = game.transform.flip(PLAYER_SATYR_TURRET, True, False)
PLAYER_GOLEM_TURRET = game.image.load("Resources/golem_turret.png").convert_alpha()
PLAYER_GOLEM_TURRET = game.transform.scale(PLAYER_GOLEM_TURRET, (4 * CELL, 4 * CELL))
ENEMY_GOLEM_TURRET = game.transform.flip(PLAYER_GOLEM_TURRET, True, False)
PLAYER_ELF_TURRET = game.image.load("Resources/elf_turret.png").convert_alpha()
PLAYER_ELF_TURRET = game.transform.scale(PLAYER_ELF_TURRET, (4 * CELL, 4 * CELL))
ENEMY_ELF_TURRET = game.transform.flip(PLAYER_ELF_TURRET, True, False)
SELL_BUTTON = game.image.load("Resources/dollar-symbol.png").convert_alpha()
REPAIR_BUTTON = game.image.load("Resources/tool.png").convert_alpha()
SATYR_CANNONBALL= game.image.load("Resources/satyr_cannonball.png").convert_alpha()
SATYR_CANNONBALL = game.transform.scale(SATYR_CANNONBALL, (1 * CELL, 1 * CELL))
GOLEM_CANNONBALL = game.image.load("Resources/golem_cannonball.png").convert_alpha()
GOLEM_CANNONBALL =  game.transform.scale(GOLEM_CANNONBALL, (1 * CELL, 1 * CELL))
ELF_CANNONBALL = game.image.load("Resources/elf_cannonball.png").convert_alpha()
ELF_CANNONBALL = game.transform.scale(ELF_CANNONBALL, (1 * CELL, 1 * CELL))
UPGRADE_BUTTON = game.image.load("Resources/upgrade_button.png").convert_alpha()
GAME_OVER = game.image.load("Resources/game_over.png").convert_alpha()
GAME_WON = game.image.load("Resources/game_won.png").convert_alpha()