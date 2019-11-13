from rest_framework.response import Response
from rest_framework import status

class PadronizacaoResponse():
    
    def __init__(self):
        self.__status = {200: status.HTTP_200_OK, 
                         201: status.HTTP_201_CREATED, 
                         202: status.HTTP_202_ACCEPTED,
                         400: status.HTTP_400_BAD_REQUEST, 
                         403: status.HTTP_403_FORBIDDEN, 
                         404: status.HTTP_404_NOT_FOUND,
                         422: status.HTTP_422_UNPROCESSABLE_ENTITY
                        }
    
    def responseFormatado(self, possui_dados, status_code, data=None, mensagem=None):
        '''
            Padronização da estrutura de reponse:
            
            - sucesso = Boolean
            - status_code = int
            - data = serializer
            - mensagem = string
        '''
        
        self.retorno = {'data':None, 'mensagem': None}

        if possui_dados:
            if not data:
                raise Exception
            self.retorno['data'] = data
        else:
            if not mensagem:
                raise Exception
            self.retorno['mensagem'] = mensagem
            
        status = self.__getStatus(status_code)
        return Response(self.retorno, status=status)
    
    def __getStatus(self, status):
        return self.__status[status]

    
