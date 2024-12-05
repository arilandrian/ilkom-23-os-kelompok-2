<?php
session_start();

if (!isset($_SESSION['data'])) {
    $_SESSION['data'] = [];
}

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['new_item'])) {
    $new_item = htmlspecialchars($_POST['new_item']);
    $_SESSION['data'][] = $new_item;
}
?>

<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1 {
            color: #333;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            background: #f4f4f4;
            margin: 5px 0;
            padding: 10px;
            border-radius: 5px;
        }
    </style>
</head>
<body>

<h1>Dashboard</h1>

<h2>Lihat Data</h2>
<ul>
    <?php if (empty($_SESSION['data'])): ?>
        <li>Tidak ada data untuk ditampilkan.</li>
    <?php else: ?>
        <?php foreach ($_SESSION['data'] as $index => $item): ?>
            <li><?php echo ($index + 1) . ". " . $item; ?></li>
        <?php endforeach; ?>
    <?php endif; ?>
</ul>

<h2>Tambah Data</h2>
<form method="POST" action="">
    <input type="text" name="new_item" required>
    <button type="submit">Tambah</button>
</form>

</body>
</html>