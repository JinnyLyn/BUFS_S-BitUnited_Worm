<?php 

if (!defined('ALLOW_INCLUDE')) {
    http_response_code(403);
    exit('Direct access is not allowed.');
} else {
    $file = file_get_contents('/flag');
    echo trim($file); 
}


?>