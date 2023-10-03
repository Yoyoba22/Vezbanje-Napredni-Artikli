CREATE TABLE Artikal(
sifra_artikla SERIAL PRIMARY KEY,
naziv VARCHAR(50) NOT NULL,
kolicina INT NOT NULL,
cena FLOAT NOT NULL);


INSERT INTO Artikal (sifra_artikla,naziv,kolicina,cena) 
VALUES 
		(1,'koka kola',40,70.00),
		(2,'kisela voda',10,50.00),
		(3,'Fanta',25,60.00),
		(4,'Kafa',20,15.00),
		(5,'Stella',35,120.00),
		(6,'Jelen',55,90.00),
		(7,'Somersby',30,130.50);


SELECT * FROM Artikal