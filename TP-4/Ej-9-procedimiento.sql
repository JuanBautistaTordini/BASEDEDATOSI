DELIMITER //

CREATE PROCEDURE GenerarFacturas()
BEGIN 
    DECLARE PedidoIdV INT;
    DECLARE ClienteIdV INT;
    DECLARE TotalPedidoV DECIMAL(10,2);
    DECLARE done INT DEFAULT FALSE;
    
    DECLARE cursor_pedidos CURSOR FOR
        SELECT PedidoId, ClienteId, TotalPedido 
        FROM Pedidos
        WHERE Facturado = 0;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cursor_pedidos;

    START TRANSACTION;

    FETCH cursor_pedidos INTO PedidoIdV, ClienteIdV, TotalPedidoV;

    WHILE NOT done DO
 
        INSERT INTO Facturas (PedidoId, FechaFactura, MontoFacturado)
        VALUES (PedidoIdV, CURRENT_DATE, TotalPedidoV);

        UPDATE Pedidos
        SET Facturado = 1
        WHERE PedidoId = PedidoIdV;

        FETCH cursor_pedidos INTO PedidoIdV, ClienteIdV, TotalPedidoV;
    END WHILE;


    CLOSE cursor_pedidos;

    COMMIT;
END//

DELIMITER ;


