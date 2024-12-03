
import random
import base
#x, y, name 是构造函数的参数，分别表示AI的初始位置和名称，传递给父类base.Enemy
class FunModeAI(base.Enemy):
    def __init__(self, x, y, name):
        super().__init__(x, y, name)

    def perform_turn(self, game_manager):
        """
        趣味模式下的AI决策逻辑：
        - 抽牌：从牌堆中抽取 1 到 3 张牌，排除场上玩家手牌。
        - 出牌：优先出掉颜色相同且数字连续的牌组（如果共用牌在多个组中）。
        - 如果没有操作可以执行，返回 ["finish"]。
        """
        # 1. 抽牌策略
        #从game_manager.cards中找出当前可以抽的牌，排除所有玩家的手牌（调用get_all_players_hands方法）。
        #如果牌堆中有可抽的牌，并且当前游戏允许抽牌（game_manager.draw为真），则随机抽取1到3张牌。
        #抽牌后返回操作信息，例如["draw", 2]表示抽了两张牌
        available_cards = [card for card in game_manager.cards if card not in self.get_all_players_hands(game_manager)]
        if available_cards and game_manager.draw:
            draw_count = random.randint(1, 3)
            draw_cards = random.sample(available_cards, min(draw_count, len(available_cards)))
            self.add(draw_cards)
            # print(f"{self.name} drew {len(draw_cards)} card(s): {', '.join(str(c) for c in draw_cards)}")
            return ["draw", len(draw_cards)]

        # 2. 出牌策略
        #调用generate_valid_groups生成当前手牌中的所有有效牌组。
        #如果存在有效组：
        #优先选择包含共享卡牌的组（调用find_shared_card_groups）。
        #在共享卡牌组中，优先选择颜色相同且数字连续的组（调用is_color_same_and_consecutive）。
        #返回出牌操作，例如["discard", selected_group]。
        valid_groups = self.generate_valid_groups()
        if valid_groups:
            # 查找共用牌的有效组
            shared_card_groups = self.find_shared_card_groups(valid_groups)
            if shared_card_groups:
                # 优先选择颜色相同且数字连续的组
                color_same_groups = [
                    group for group in shared_card_groups if self.is_color_same_and_consecutive(group)
                ]
                if color_same_groups:
                    selected_group = color_same_groups[0]
                else:
                    selected_group = shared_card_groups[0]
                # 移除选中的组
                # self.remove(selected_group)
                # game_manager.cards.extend(selected_group)
                # print(f"{self.name} discarded: {', '.join(str(c) for c in selected_group)}")
                return ["discard", selected_group]

        # 3. 回合结束
        # print(f"{self.name} finished the turn.")
        return ["finish", 0]

    def get_all_players_hands(self, game_manager):
        """
        获取场上所有玩家手牌的集合，用于排除牌堆中的这些牌。
        """
        all_hands = []
        all_hands.extend(game_manager.player.hands)
        for enemy in game_manager.enemies:
            all_hands.extend(enemy.hands)
        return all_hands

    def generate_valid_groups(self):
        """
        根据手牌生成所有可能的有效牌组：
        - 连续三个数字的牌，颜色相同。
        - 相同数字的三张牌，颜色可以不同。
        """
        groups = []
        # 按颜色连续数字
        colours = set(card.colour for card in self.hands)
        for colour in colours:
            cards = [card for card in self.hands if card.colour == colour]
            cards.sort(key=lambda c: c.number)
            for i in range(len(cards) - 2):
                if (cards[i + 1].number == cards[i].number + 1 and
                        cards[i + 2].number == cards[i].number + 2):
                    groups.append([cards[i], cards[i + 1], cards[i + 2]])

        # 按数字相同不同颜色
        numbers = set(card.number for card in self.hands)
        for number in numbers:
            cards = [card for card in self.hands if card.number == number]
            if len(cards) >= 3:
                groups.append(cards[:3])

        return groups

    def find_shared_card_groups(self, groups):
        """
        查找含有共用卡牌的有效组（卡牌在多个组中）。
        """
        card_count = {}
        for group in groups:
            for card in group:
                card_count[card] = card_count.get(card, 0) + 1
        shared_cards = {card for card, count in card_count.items() if count > 1}

        shared_card_groups = [group for group in groups if any(card in shared_cards for card in group)]
        return shared_card_groups

    def is_color_same_and_consecutive(self, group):
        """
        判断牌组是否颜色相同且数字连续。
        """
        if len(set(card.colour for card in group)) == 1:  # 颜色相同
            numbers = sorted(card.number for card in group)
            return all(numbers[i + 1] == numbers[i] + 1 for i in range(len(numbers) - 1))
        return False



