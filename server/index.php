<?php
if(isset($_POST['data'])){
    file_put_contents(realpath('./banner.txt'),$_POST['data']);
}
?>
<form method="post">
<input name="data" value="<?php echo file_get_contents(realpath('./banner.txt')) ?>"/>
    <input type="submit"/>
</form>
