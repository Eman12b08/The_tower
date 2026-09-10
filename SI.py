class SI:
    def __init__(self):
        import pygame

        nf=1.3
        sf=(0,0,0)
        pygame.init()
        screen = pygame.display.set_mode((int(210*nf), int(460*nf)))
        pygame.display.set_caption("Gioco")
        screen.fill(sf)

        sb=pygame.transform.scale(pygame.image.load("sb.png").convert_alpha(),(int(210*nf), int(460*nf)))
        screen.blit(sb,(0,0))

        play=pygame.transform.scale(pygame.image.load("play.png").convert_alpha(),(int(170*nf), int(60*nf)))
        pl=screen.blit(play,(20,200))

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = event.pos
                    if pl.collidepoint(mx,my):
                        run=False
                        break