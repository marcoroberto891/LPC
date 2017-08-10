import self as self


class Pessoa():
    nome = ''
    data_nascimento = None

    def __init__(self, nome, idade, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

    def __str__(self):
        return self.nome

class Endereco(object):
    logradouro = None
    def __init__(self, logradouro):
        self.logradouro = logradouro

    self.logradouro = logradouro


class PessoaFisica(Pessoa):
    def __init__(self, cpf, nome, data_nascimento):
        Pessoa.__init__(self, nome, data_nascimento)
        self.cpf = cpf

    def __str__(self):
        return u'{} - {}'.format(self.cpf, self.nome)

class PessoaJuridica(Pessoa):

    def __init__(self, cnpj, nome, data_nascimento):
        Pessoa.__init__(self,nome.idade)
        self.cnpj = cnpj


class Pessoa(object):
    nome = ''
    data_nascimento = None

    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = Endereco('rua 1')

        def __str__(self):
            return self.nome

