<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Loader</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            width: 100%;
        }
        h1 {
            color: #333;
        }
        p {
            color: #555;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>File Content Viewer</h1>
        <?php
        
        define('ALLOW_INCLUDE', true);

        if (isset($_GET['file'])) {
            $encodedFileName = $_GET['file'];
            if (stripos($encodedFileName, "Li4v") !== false){
                echo "<p class='error'>Error: Not allowed ../.</p>";
                exit(0);
            }
            if ((stripos($encodedFileName, "ZmxhZ") !== false) || (stripos($encodedFileName, "aHA=") !== false)){
                echo "<p class='error'>Error: Not allowed flag.</p>";
                exit(0);
            }
            $decodedFileName = base64_decode($encodedFileName);

            $filePath = __DIR__ . DIRECTORY_SEPARATOR . $decodedFileName;

            if ($decodedFileName && file_exists($filePath) && strpos(realpath($filePath),__DIR__) == 0) {
                echo "<p>Including file: <strong>$decodedFileName</strong></p>";
                echo "<div>";
                require_once($decodedFileName);
                echo "</div>";
            } else {
                echo "<p class='error'>Error: Invalid file or file does not exist.</p>";
            }
        } else {
            echo "<p class='error'>No file parameter provided.</p>";
        }
        ?>
    </div>
</body>
</html>
