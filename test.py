import pygame

pygame.init()

# Créer une fenêtre
window = pygame.display.set_mode((400, 300))

# Dictionnaire pour stocker l'état des touches
keys = {}

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # Mettre à jour l'état de la touche enfoncée
            keys[event.key] = True
            print("La touche", pygame.key.name(event.key), "est enfoncée.")

        if event.type == pygame.KEYUP:
            # Mettre à jour l'état de la touche relâchée
            keys[event.key] = False
            print("La touche", pygame.key.name(event.key), "est relâchée.")

    # Mettre à jour la fenêtre
    pygame.display.update()

pygame.quit()