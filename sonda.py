

class sonda():
    # classe principal
    def __init__(self, x, y, orientacao):
        self.x = x
        self.y = y        
        self.orientacao = orientacao
        

        print ("Posicao_origem:", self.x, self.y, self.orientacao)

    # FUNCAO PARA GIRAR A SONDA EM 90 GRAUS.
    def girar(self,comando):

        if comando == 'L':
            if self.orientacao == 'N':
              self.orientacao = 'W'
            
            elif self.orientacao == 'S':
              self.orientacao = 'E'
              

            elif self.orientacao == 'W':
              self.orientacao = 'S'
              

            elif self.orientacao == 'E': 
              self.orientacao = 'N'
      
              
        else:
            if self.orientacao == 'N':
              self.orientacao = 'E'
              

            elif self.orientacao == 'S':
              self.orientacao = 'W'
              

            elif self.orientacao == 'W':
              self.orientacao = 'N'
              

            elif self.orientacao == 'E':
              self.orientacao = 'S'
                    
    
    # FUNCAO PARA FAZER A SONDA ANDAR
    def walk(self,comando):

        if self.orientacao == 'N':

          self.y += 1

        elif self.orientacao == 'S':
          
          self.y -= 1

        elif self.orientacao == 'E':

          self.x += 1

        elif self.orientacao == 'W':

          self.x -= 1

    # FUNCAO PARSE (JOIN GIRAR E ANDAR)
    def parse(self,comando):

      for c in comando:

        if c == "L" or c == "R":

          self.girar(c)

        elif c == "M":

          self.walk(c)

    def output(self):
        return "Posicao_destino:", self.x, self.y, self.orientacao
