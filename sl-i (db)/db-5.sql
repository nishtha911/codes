--create tables first:
CREATE TABLE O_Roll_Call (
    roll_no INT PRIMARY KEY,
    student_name VARCHAR(50)
);

CREATE TABLE N_Roll_Call (
    roll_no INT PRIMARY KEY,
    student_name VARCHAR(50)
);

--insert some values:
INSERT INTO O_Roll_Call VALUES (1, 'Anurag'), (2, 'Palash'), (3, 'Vipul');
INSERT INTO N_Roll_Call VALUES (4, 'Vedant'), (5, 'Ananya'), (6, 'Nishtha');

--then run this stored procedure:

DELIMITER $$

CREATE PROCEDURE Merge_Roll_Call()
BEGIN
    DECLARE v_roll INT;
    DECLARE v_name VARCHAR(50);
    DECLARE done INT DEFAULT 0;

    DECLARE cur_roll CURSOR FOR 
        SELECT roll_no, student_name FROM N_Roll_Call;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN cur_roll;

    merge_loop: LOOP
        FETCH cur_roll INTO v_roll, v_name;
        IF done = 1 THEN 
            LEAVE merge_loop;
        END IF;

        IF NOT EXISTS (SELECT 1 FROM O_Roll_Call WHERE roll_no = v_roll) THEN
            INSERT INTO O_Roll_Call (roll_no, student_name)
            VALUES (v_roll, v_name);
        END IF;
    END LOOP;

    CLOSE cur_roll;
END$$

DELIMITER ;

--execute it:
CALL Merge_Roll_Call();
SELECT * FROM O_Roll_Call; --check output


