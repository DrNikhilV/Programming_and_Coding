<?php
class Records {
    private $conn;
    private $recordsTable = 'live_records';

    public $id;
    public $name;
    public $age;
    public $skills;
    public $address;
    public $designation;

    public function __construct($db) {
        $this->conn = $db;
    }

    // List all records with search, order and pagination
    public function listRecords() {
        $sqlQuery = "SELECT * FROM " . $this->recordsTable;

        if (!empty($_POST["search"]["value"])) {
            $sqlQuery .= ' WHERE (id LIKE "%' . $_POST["search"]["value"] . '%" ';
            $sqlQuery .= ' OR name LIKE "%' . $_POST["search"]["value"] . '%" ';
            $sqlQuery .= ' OR designation LIKE "%' . $_POST["search"]["value"] . '%" ';
            $sqlQuery .= ' OR address LIKE "%' . $_POST["search"]["value"] . '%" ';
            $sqlQuery .= ' OR skills LIKE "%' . $_POST["search"]["value"] . '%") ';
        }

        if (!empty($_POST["order"])) {
            $orderColumn = intval($_POST['order']['0']['column']);
            $orderDir = $_POST['order']['0']['dir'] === 'desc' ? 'DESC' : 'ASC';
            $columns = ['id', 'name', 'skills', 'address', 'designation', 'age'];
            $sqlQuery .= " ORDER BY " . $columns[$orderColumn] . " " . $orderDir;
        } else {
            $sqlQuery .= " ORDER BY id DESC";
        }

        if ($_POST["length"] != -1) {
            $start = intval($_POST["start"]);
            $length = intval($_POST["length"]);
            $sqlQuery .= " LIMIT " . $start . ", " . $length;
        }

        $stmt = $this->conn->prepare($sqlQuery);
        $stmt->execute();
        $result = $stmt->get_result();

        $stmtTotal = $this->conn->prepare("SELECT * FROM " . $this->recordsTable);
        $stmtTotal->execute();
        $allResult = $stmtTotal->get_result();

        $allRecords = $allResult->num_rows;
        $displayRecords = $result->num_rows;
        $records = array();

        while ($record = $result->fetch_assoc()) {
            $rows = array();
            $rows[] = $record['id'];
            $rows[] = htmlspecialchars($record['name']);
            $rows[] = htmlspecialchars($record['skills']);
            $rows[] = htmlspecialchars($record['address']);
            $rows[] = htmlspecialchars($record['designation']);
            $rows[] = intval($record['age']);
            $rows[] = '<button type="button" name="update" id="'.$record['id'].'" class="btn btn-warning btn-xs update">Edit</button>';
            $rows[] = '<button type="button" name="delete" id="'.$record['id'].'" class="btn btn-danger btn-xs delete">Delete</button>';
            $records[] = $rows;
        }

        $output = array(
            "draw" => intval($_POST["draw"]),
            "recordsTotal" => $allRecords,
            "recordsFiltered" => $allRecords,
            "data" => $records
        );

        echo json_encode($output);
    }

    // Add new record
    public function addRecord() {
        $stmt = $this->conn->prepare("INSERT INTO ".$this->recordsTable." (name, skills, address, designation, age) VALUES (?, ?, ?, ?, ?)");
        $this->name = htmlspecialchars(strip_tags($this->name));
        $this->skills = htmlspecialchars(strip_tags($this->skills));
        $this->address = htmlspecialchars(strip_tags($this->address));
        $this->designation = htmlspecialchars(strip_tags($this->designation));
        $this->age = intval($this->age);
        $stmt->bind_param("ssssi", $this->name, $this->skills, $this->address, $this->designation, $this->age);
        if($stmt->execute()){
            return true;
        }
        return false;
    }

    // Get a single record by ID
    public function getSingleRecord() {
        $stmt = $this->conn->prepare("SELECT * FROM ".$this->recordsTable." WHERE id = ?");
        $this->id = intval($this->id);
        $stmt->bind_param("i", $this->id);
        $stmt->execute();
        $result = $stmt->get_result();
        if($result->num_rows > 0){
            return $result->fetch_assoc();
        }
        return null;
    }

    // Update an existing record
    public function updateRecord() {
        $stmt = $this->conn->prepare("UPDATE ".$this->recordsTable." SET name = ?, skills = ?, address = ?, designation = ?, age = ? WHERE id = ?");
        $this->name = htmlspecialchars(strip_tags($this->name));
        $this->skills = htmlspecialchars(strip_tags($this->skills));
        $this->address = htmlspecialchars(strip_tags($this->address));
        $this->designation = htmlspecialchars(strip_tags($this->designation));
        $this->age = intval($this->age);
        $this->id = intval($this->id);
        $stmt->bind_param("ssssii", $this->name, $this->skills, $this->address, $this->designation, $this->age, $this->id);
        if($stmt->execute()){
            return true;
        }
        return false;
    }

    // Delete a record by ID
    public function deleteRecord() {
        if($this->id){
            $stmt = $this->conn->prepare("DELETE FROM ".$this->recordsTable." WHERE id = ?");
            $this->id = intval($this->id);
            $stmt->bind_param("i", $this->id);
            if($stmt->execute()){
                return true;
            }
        }
        return false;
    }
}
?>
