<?php
include_once 'config/Database.php';
include_once 'Class/Records.php';

$database = new Database();
$db = $database->getConnection();
$record = new Records($db);

if(isset($_POST['action'])) {
    if($_POST['action'] == 'listRecords') {
        $record->listRecords();
    }

    if($_POST['action'] == 'addRecord') {
        $record->name = $_POST['name'];
        $record->skills = $_POST['skills'];
        $record->address = $_POST['address'];
        $record->designation = $_POST['designation'];
        $record->age = $_POST['age'];
        if($record->addRecord()){
            echo 'Record Added Successfully';
        }
    }

    if($_POST['action'] == 'getRecord') {
        $record->id = $_POST['id'];
        $result = $record->getSingleRecord();
        echo json_encode($result);
    }

    if($_POST['action'] == 'updateRecord') {
        $record->id = $_POST['id'];
        $record->name = $_POST['name'];
        $record->skills = $_POST['skills'];
        $record->address = $_POST['address'];
        $record->designation = $_POST['designation'];
        $record->age = $_POST['age'];
        if($record->updateRecord()){
            echo 'Record Updated Successfully';
        }
    }

    if($_POST['action'] == 'deleteRecord') {
        $record->id = $_POST['id'];
        if($record->deleteRecord()){
            echo 'Record Deleted Successfully';
        }
    }
}
?>
