#imports
import discord
import os

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):

    if '!disciplinas1periodo' in message.content.lower():
            await message.channel.send('Disciplinas Ciencia da Computação Unit/AL - Primeiro Período')
            await message.channel.send('Fundamentos de Programação')
            await message.channel.send('Inglês para Computação')
            await message.channel.send('Fundamentos de Matemática Computacional')
            await message.channel.send('Fundamentos P.C e A de Computadores')
            await message.channel.send('Filosofia e Cidadania')

    if '!disciplinas2periodo' in message.content.lower():
            await message.channel.send('Disciplinas Ciencia da Computação Unit/AL - Segundo Período')
            await message.channel.send('Cálculo para Computação 1')
            await message.channel.send('Laboratório de Programação')
            await message.channel.send('Fundamentos Antropológicos e Sociológicos')
            await message.channel.send('Experiência Extensionista I')
            await message.channel.send('Redes de Computadores')
    
    if '!disciplinas3periodo' in message.content.lower():
            await message.channel.send('Disciplinas Ciencia da Computação Unit/AL - Terceiro Período')
            await message.channel.send('Sistemas Digitais')
            await message.channel.send('Projeto de Programação')
            await message.channel.send('Estatística Computacional')
            await message.channel.send('Cálculo para Computação II')
            await message.channel.send('Metodologia Científica')

    if '!disciplinas4periodo' in message.content.lower():
            await message.channel.send('Disciplinas Ciencia da Computação Unit/AL - Quarto Período')
            await message.channel.send('Estrutura de Dados')
            await message.channel.send('Laboratório de Redes de Computadores')
            await message.channel.send('Teoria dos Grafos')
            await message.channel.send('Engenharia de Software')
            await message.channel.send('Cloud Computing')
        
    if '!disciplinas5periodo' in message.content.lower():
            await message.channel.send('Disciplinas Ciencia da Computação Unit/AL - Quinto Período')
            await message.channel.send('Modelagem de Dados')
            await message.channel.send('Estrutura de Dados Avançada')
            await message.channel.send('Laboratório de Engenharia de Software')
            await message.channel.send('Laboratório de Análise de Algoritmo')
            await message.channel.send('Teoria da Computação')

    if '!disciplinas6periodo' in message.content.lower():
        await message.channel.send('Disciplinas Ciencia da Computação Unit/AL - Sexto Período')
        await message.channel.send('Linguagens Formais e Autômatos')
        await message.channel.send('Sistemas Operacionais')
        await message.channel.send('Inteligência Artificial')
        await message.channel.send('Experiência Extensionista II')
        await message.channel.send('Optativa 1')

    if '!disciplinas7periodo' in message.content.lower():
        await message.channel.send('Disciplinas Ciencia da Computação Unit/AL - Sétimo Período')
        await message.channel.send('Interface Humano Computador')
        await message.channel.send('Machine Learning')
        await message.channel.send('Compiladores')
        await message.channel.send('Laboratório de Banco de Dados')
        await message.channel.send('Experiência Extensionista III')

    if '!disciplinas8periodo' in message.content.lower():
        await message.channel.send('Disciplinas Ciencia da Computação Unit/AL - Oitavo Período')
        await message.channel.send('Processamento de Imagens de Computação Gráfica')
        await message.channel.send('Programação Avançada')
        await message.channel.send('Project LAB')
        await message.channel.send('Experiência Extensionista IV')
        await message.channel.send('Optativa 2')

    if '!disciplinas9periodo' in message.content.lower():
        await message.channel.send('Disciplinas Ciencia da Computação Unit/AL - Nono Período')
        await message.channel.send('TCC')
        await message.channel.send('Estágio Supervisionado')
        await message.channel.send('Direito Digital')
        await message.channel.send('Experiência Extensionista')

    if '!magister' in message.content.lower():
        await message.channel.send('Link de acesso ao Magister: https://wwws.fits.edu.br/Portal/Index.jsp')

    if '!ava' in message.content.lower():
        await message.channel.send('Link de acesso ao Ava: https://ava.grupotiradentes.com/shared/online/login.html')

    if '!disciplinasoptativas6periodo' in message.content.lower():
        await message.channel.send('Empreendedorismo')
        await message.channel.send('História e Cultura Afro-Brasileira e Africana')
        await message.channel.send('Libras')
        await message.channel.send('Relações Étnico-Raciais')

    if '!disciplinasoptativas8periodo' in message.content.lower():
        await message.channel.send('Big Data Analysis')
        await message.channel.send('Desenvolvimento para Dispositivos Móveis')
        await message.channel.send('Programação Web')
        await message.channel.send('Tópicos Especiais em Computação')

    if '!portalunit' in message.content.lower():
        await message.channel.send('Portal da Universidade Tiradentes: https://al.unit.br/')
    
    
client.run(TOKEN)