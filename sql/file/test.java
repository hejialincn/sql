package com.example.modid; // 替换为你的包名，确保与 modid 匹配

import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.event.player.AttackEntityCallback;
import net.minecraft.entity.EntityType;
import net.minecraft.entity.SpawnGroup;
import net.minecraft.entity.SpawnRestriction;
import net.minecraft.entity.attribute.DefaultAttributeContainer;
import net.minecraft.entity.attribute.EntityAttributes;
import net.minecraft.item.ArmorItem;
import net.minecraft.item.ArmorMaterial;
import net.minecraft.item.ElytraItem;
import net.minecraft.item.Item;
import net.minecraft.item.ItemStack;
import net.minecraft.item.SwordItem;
import net.minecraft.item.ToolMaterial;
import net.minecraft.util.ActionResult;
import net.minecraft.util.Identifier;
import net.minecraft.util.registry.Registry;
import net.minecraft.world.Heightmap;
import net.minecraft.world.biome.Biome;
import net.minecraft.world.biome.SpawnSettings;

public class MyMod implements ModInitializer {

    // 注册生物的 ID
    private static final Identifier POISON_SNAKE_ID = new Identifier("modid", "poison_snake");
    // 注册物品的 ID
    private static final Identifier EVIL_SNAKE_MARK_ID = new Identifier("modid", "evil_snake_mark");

    @Override
    public void onInitialize() {
        // 注册生物实体
        Registry.register(Registry.ENTITY_TYPE, POISON_SNAKE_ID, EntityType.Builder.create(EntityPoisonSnake::new, SpawnGroup.MONSTER)
                .setDimensions(0.6F, 0.5F) // 生物大小
                .build(POISON_SNAKE_ID.toString()));

        // 设置生物生成规则
        SpawnSettings.Builder spawnSettings = new SpawnSettings.Builder();
        spawnSettings.spawn(SpawnGroup.MONSTER, new SpawnSettings.SpawnEntry(POISON_SNAKE_ID, 10, 1, 3));

        // 将生物生成规则添加到生物群系
        for (Biome biome : Registry.BIOME) {
            biome.getSpawnSettings().addSpawn(SpawnGroup.MONSTER, spawnSettings.build());
        }

        // 注册生物属性
        DefaultAttributeContainer.Builder attributeBuilder = HostileEntity.createHostileAttributes();
        attributeBuilder.add(EntityAttributes.GENERIC_MAX_HEALTH, 100.0); // 血量为100
        attributeBuilder.add(EntityAttributes.GENERIC_ATTACK_DAMAGE, 5.0); // 攻击伤害为5
        EntityType.Builder.create(EntityPoisonSnake::new, SpawnGroup.MONSTER)
                .setDefaultAttributes(attributeBuilder.build());

        // 注册物品
        Registry.register(Registry.ITEM, EVIL_SNAKE_MARK_ID, new ItemEvilSnakeMark(new Item.Settings().group(ItemGroup.MISC)));

        // 注册盔甲、武器和鞘翅的实现类
        Registry.register(Registry.ITEM, new Identifier("modid", "custom_helmet"), new CustomArmorItem(ArmorMaterial.IRON, EquipmentSlot.HEAD, new Item.Settings().group(ItemGroup.COMBAT)));
        Registry.register(Registry.ITEM, new Identifier("modid", "custom_chestplate"), new CustomArmorItem(ArmorMaterial.IRON, EquipmentSlot.CHEST, new Item.Settings().group(ItemGroup.COMBAT)));
        Registry.register(Registry.ITEM, new Identifier("modid", "custom_leggings"), new CustomArmorItem(ArmorMaterial.IRON, EquipmentSlot.LEGS, new Item.Settings().group(ItemGroup.COMBAT)));
        Registry.register(Registry.ITEM, new Identifier("modid", "custom_boots"), new CustomArmorItem(ArmorMaterial.IRON, EquipmentSlot.FEET, new Item.Settings().group(ItemGroup.COMBAT)));
        
        Registry.register(Registry.ITEM, new Identifier("modid", "custom_sword"), new CustomSwordItem(ToolMaterial.IRON, 3, -2.4F, new Item.Settings().group(ItemGroup.COMBAT)));
        Registry.register(Registry.ITEM, new Identifier("modid", "custom_elytra"), new CustomElytraItem(new Item.Settings().group(ItemGroup.TRANSPORTATION)));

        // 在击败生物时发送消息，这里使用之前的代码示例
        AttackEntityCallback.EVENT.register((player, world, hand, entity, hitResult) -> {
            if (entity instanceof EntityPoisonSnake)
	    {
                player.sendMessage(new LiteralText("你击败了一个毒蛇！"), false);
                // 添加掉落物到玩家背包
                player.getInventory().insertStack(new ItemStack(ItemRegistry.EVIL_SNAKE_MARK));
	    } 
	    else 
	    {
                player.sendMessage(new LiteralText("你击败了一个生物！"), false);
            }
            return ActionResult.SUCCESS;
        });
    }
}

