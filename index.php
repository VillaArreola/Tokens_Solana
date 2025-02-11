<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Listado de Monedas</title>
    <link rel="stylesheet" href="css/style.css"> <!-- Opcional: Enlaza tu archivo CSS -->
</head>
<body>
    <h1>Listado de Monedas</h1>
    <table border="1">
        <thead>
            <tr>
                <th>Nombre</th>
                <th>Símbolo</th>
                <th>Contrato</th>
                <th>Marketcap</th>
                <th>Máximo Precio (ATH)</th>
            </tr>
        </thead>
        <tbody>
            <?php
            // Conectar a la base de datos SQLite
            $db_path = 'db/cryptos.db'; // Ruta a la base de datos
            try {
                $db = new PDO("sqlite:$db_path");
                $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

                // Consulta para obtener los datos de la tabla
                $query = "SELECT name, symbol, contract_address, marketcap, mc_ath FROM cryptos";
                $result = $db->query($query);

                // Mostrar los datos en la tabla
                foreach ($result as $row) {
                    echo "<tr>";
                    echo "<td>" . htmlspecialchars($row['name']) . "</td>";
                    echo "<td>" . htmlspecialchars($row['symbol']) . "</td>";
                    echo "<td>" . htmlspecialchars($row['contract_address']) . "</td>";
                    echo "<td>" . htmlspecialchars($row['marketcap']) . "</td>";
                    echo "<td>" . htmlspecialchars($row['mc_ath']) . "</td>";
                    echo "</tr>";
                }
            } catch (PDOException $e) {
                echo "<tr><td colspan='5'>Error al conectar a la base de datos: " . $e->getMessage() . "</td></tr>";
            }
            ?>
        </tbody>
    </table>
</body>
</html>