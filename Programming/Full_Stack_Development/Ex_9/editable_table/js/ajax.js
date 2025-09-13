$(document).ready(function(){
    var dataRecords = $('#recordListing').DataTable({
        "processing": true,
        "serverSide": true,
        "ajax": {
            url: "ajax_action.php",
            type: "POST",
            data: { action: 'listRecords' }
        },
        "columnDefs": [
            { "orderable": false, "targets": [6, 7] }
        ]
    });

    $('#add_record').click(function(){
        $('#recordForm')[0].reset();
        $('#recordModal .modal-title').text("Add Record");
        $('#action').val("addRecord");
        $('#save').val("Add");
        $('#recordModal').modal('show');
    });

    $('#recordForm').on('submit', function(event){
        event.preventDefault();
        $.ajax({
            url: "ajax_action.php",
            method: "POST",
            data: $(this).serialize(),
            success: function(data){
                $('#recordForm')[0].reset();
                $('#recordModal').modal('hide');
                dataRecords.ajax.reload();
                alert(data);
            }
        });
    });

    $('#recordListing').on('click', '.update', function(){
        var id = $(this).attr("id");
        $.ajax({
            url: "ajax_action.php",
            method: "POST",
            data: {id: id, action: 'getRecord'},
            dataType: "json",
            success: function(data){
                $('#recordModal').modal('show');
                $('#name').val(data.name);
                $('#skills').val(data.skills);
                $('#address').val(data.address);
                $('#designation').val(data.designation);
                $('#age').val(data.age);
                $('#id').val(data.id);
                $('#recordModal .modal-title').text("Edit Record");
                $('#action').val("updateRecord");
                $('#save').val("Update");
            }
        });
    });

    $('#recordListing').on('click', '.delete', function(){
        var id = $(this).attr("id");
        if(confirm("Are you sure you want to delete this record?")) {
            $.ajax({
                url: "ajax_action.php",
                method: "POST",
                data: {id: id, action: 'deleteRecord'},
                success: function(data){
                    dataRecords.ajax.reload();
                    alert(data);
                }
            });
        } else {
            return false;
        }
    });
});
