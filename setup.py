import os

pasta = 'C:/Projects/Python/Desktop/academicotech/list7'

if not os.path.exists(pasta):
	os.makedirs(pasta)

qtd_files = 5
for i in range(qtd_files):
	file_name = f'ex{i+1}.py'
	file_way = os.path.join(pasta, file_name)
	with open(file_way, 'w') as file:
		file.write(f'Conteudo do arquivo {i+1}')

print(f'{qtd_files} arquivos foram criados na pasta')