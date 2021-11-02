SELECT * FROM tabela_de_produtos;

SELECT * FROM tabela_de_produtos LIMIT 5;

SELECT * FROM tabela_de_produtos LIMIT 2, 3;

SELECT * FROM tabela_de_produtos LIMIT 0, 3;

SELECT * FROM notas_fiscais;

SELECT * FROM notas_fiscais WHERE DATA_VENDA IN ('2017-01-01') LIMIT 10;
