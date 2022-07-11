<?php

if ($_GET['location'] != '') {
	if ($_GET['location'] > 12) {
		echo extractFile('phdata.csv', $_GET['location'], 13);
	} else {
		echo extractFile('cadata.csv', $_GET['location'], 0);
	}
}

function extractFile($filename, $location, $count) {
	$file = fopen($filename, "r");
	while (! feof($file)) {
		$result[] = (fgetcsv($file));	
	}
	foreach ($result as $x) {
		if ($count == $location) {
			$answer = $x;
		}
		$count++;
	}
	return json_encode($answer);
	fclose($file);
}
