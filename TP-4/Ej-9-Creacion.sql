CREATE TABLE Pedidos (
    PedidoId INT PRIMARY KEY AUTO_INCREMENT,
    ClienteId INT NOT NULL,
    FechaPedido DATE NOT NULL,
    TotalPedido DECIMAL(10,2) NOT NULL,
    Facturado BIT DEFAULT 0
);

CREATE TABLE Facturas (
    FacturaId INT PRIMARY KEY AUTO_INCREMENT,
    PedidoId INT,
    FechaFactura DATE NOT NULL,
    MontoFacturado DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (PedidoId) REFERENCES Pedidos(PedidoId)
);

