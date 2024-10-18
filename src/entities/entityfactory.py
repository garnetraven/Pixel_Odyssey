class EntityFactory:
    @staticmethod
    def create_entity(entity_type: str, groups: List[pygame.sprite.Group], parameters: Dict[str, Any]) -> Entity:
        if entity_type == 'player':
            return Player(groups, parameters['spritesheets'], parameters['position'], parameters)
        elif entity_type == 'npc':
            return NPC(groups, parameters['spritesheets'], parameters['position'], parameters)
        elif entity_type == 'enemy':
            return Enemy(groups, parameters['spritesheets'], parameters['position'], parameters)
        elif entity_type == 'block':
            return Block(groups, parameters['spritesheets'], parameters['position'], parameters)
        else:
            raise ValueError(f"Unknown entity type: {entity_type}")
