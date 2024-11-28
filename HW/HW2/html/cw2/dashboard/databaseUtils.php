<?php


class DB
{
    var $connector = null;

    function __construct($db_host, $db_user, $db_pass, $db_name, $db_port)
    {

        $this->connector = mysqli_connect($db_host, $db_user, $db_pass, $db_name, $db_port);

        if (!$this->connector) die('Connect Error (' . mysqli_connect_errno() . ') ' . mysqli_connect_error());
        mysqli_query($this->connector, "set sql_mode = ''");
        mysqli_query($this->connector, "set character set 'utf8'");
        mysqli_query($this->connector, "set names 'utf8'");

        return true;
    }

    function fetch($q)
    {
        return mysqli_fetch_assoc($q);
    }

    function get_row($q)
    {
        $result = mysqli_query($this->connector, $q);
        if (!$result) {
            die('Query Error: ' . mysqli_error($this->connector));
        }
        return mysqli_fetch_assoc($result);
    }

    function get_rows($q)
    {
        $result = mysqli_query($this->connector, $q);
        if (!$result) {
            die('Query Error: ' . mysqli_error($this->connector));
        }
        $rows = [];
        while ($row = mysqli_fetch_assoc($result)) {
            $rows[] = $row;
        }
        return $rows;
    }

    function count($q)
    {
        $result = mysqli_query($this->connector, $q);
        $count = mysqli_fetch_array($result);
        return $count[0];
    }

    function query($q)
    {
        return mysqli_query($this->connector, $q);
    }

    function escape($str)
    {
        return mysqli_real_escape_string($this->connector, $str);
    }

    function insert($q)
    {
        if (mysqli_query($this->connector, $q))
            return mysqli_insert_id($this->connector);
        return false;
    }

    function affected()
    {
        return mysqli_affected_rows($this->connector);
    }

    function insert_array($table, $array)
    {
        $q = "INSERT INTO `$table`";
        $q .= " (`" . implode("`,`", array_keys($array)) . "`) ";
        $q .= " VALUES ('" . implode("','", array_values($array)) . "') ";

        if (mysqli_query($this->connector, $q))
            return mysqli_insert_id($this->connector);
        return false;
    }

    function error()
    {
        $error = mysqli_error($this->connector);
        $errno = mysqli_errno($this->connector);
        return '[' . $errno . '] ' . $error;
    }

    function close()
    {
        $q = mysqli_close($this->connector);
        return $q;
    }

    function update($q)
    {
        $result = mysqli_query($this->connector, $q);
        if (!$result) {
            die('Query Error: ' . mysqli_error($this->connector));
        }
        return mysqli_affected_rows($this->connector) > 0;
    }


}