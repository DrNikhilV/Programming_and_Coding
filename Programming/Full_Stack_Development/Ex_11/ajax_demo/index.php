<?php
$dbhost = "localhost";
$dbuser = "root";
$dbpass = "";
$dbname = "sample";

$con = mysqli_connect($dbhost, $dbuser, $dbpass, $dbname);

if ($con->connect_error) {
    exit('Could not connect to the database: ' . $con->connect_error);
}

if (isset($_GET['q']) && !empty($_GET['q'])) {
    $cgpa = $_GET['q'];
    echo "Received CGPA: " . htmlspecialchars($cgpa) . "<br>";

    $stmt = $con->prepare("SELECT * FROM student WHERE cgpa = ?");
    $stmt->bind_param("s", $cgpa);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result && $result->num_rows > 0) {
        echo "<table border='1' style='border-collapse:collapse;'>
        <tr>
            <th style='padding:10px;'>FirstName</th>
            <th style='padding:10px;'>LastName</th>
            <th style='padding:10px;'>Rollno</th>
            <th style='padding:10px;'>CGPA</th>
        </tr>";

        while ($row = $result->fetch_assoc()) {
            echo "<tr>
            <td style='padding:10px;'>" . $row['firstname'] . "</td>
            <td style='padding:10px;'>" . $row['lastname'] . "</td>
            <td style='padding:10px;'>" . $row['rollno'] . "</td>
            <td style='padding:10px;'>" . $row['cgpa'] . "</td>
            </tr>";
        }
        echo "</table>";
    } else {
        echo "No records found for the CGPA: " . htmlspecialchars($cgpa);
    }

    $stmt->close();
} else {
    echo "Please provide a valid CGPA.";
}

mysqli_close($con);
?>
