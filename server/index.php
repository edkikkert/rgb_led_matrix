<?php
if(isset($_POST['data'])){
    $d=$_POST['data'];
    $c=$_POST['colors'];
    $t=$_POST['time'];
    $data='{"data":"'.$d.'","colors":"'.$c.'","time":'.$t.'}';
    file_put_contents(realpath('./banner.txt'),$data);
}

$con=json_decode(file_get_contents(realpath('./banner.txt')),true);
?>
<style>
input{font-family:monospace;}
</style>
<form method="post">
<input name="data" value="<?=$con['data']?>"/>&lt; text<br/>
<input name="colors" value="<?=$con['colors']?>"/>&lt; colors (r/g/b)<br/>
<input name="time" value="<?=$con['time']?>"/>&lt; time between steps (secs)<br/>
    <input type="submit"/>
</form>
