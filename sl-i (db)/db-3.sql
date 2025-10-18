DELIMITER $$

CREATE PROCEDURE Return_Book(IN p_Roll_no INT, IN p_Book VARCHAR(100))
BEGIN
    DECLARE v_Date_of_Issue DATE;
    DECLARE v_days INT;
    DECLARE v_amt DECIMAL(10,2);
    DECLARE book_not_found CONDITION FOR SQLSTATE '45000';

    DECLARE EXIT HANDLER FOR book_not_found
    BEGIN
        SELECT 'Error: Book record not found!' AS Message;
    END;

    SELECT Date_of_Issue INTO v_Date_of_Issue
    FROM Borrower
    WHERE Roll_no = p_Roll_no AND Name_of_Book = p_Book AND Status = 'I';

    IF v_Date_of_Issue IS NULL THEN
        SIGNAL book_not_found;
    END IF;

    SET v_days = DATEDIFF(CURDATE(), v_Date_of_Issue);

    IF v_days > 30 THEN
        SET v_amt = v_days * 50;
    ELSEIF v_days >= 15 THEN
        SET v_amt = v_days * 5;
    ELSE
        SET v_amt = 0;
    END IF;

    UPDATE Borrower
    SET Status = 'R'
    WHERE Roll_no = p_Roll_no AND Name_of_Book = p_Book;

    IF v_amt > 0 THEN
        INSERT INTO Fine (Roll_no, Date, Amt)
        VALUES (p_Roll_no, CURDATE(), v_amt);
    END IF;

    SELECT CONCAT('Book Returned. Fine Amount = Rs. ', v_amt) AS Result;
END$$

DELIMITER ;

CALL Return_Book(1, 'DBMS Concepts');
CALL Return_Book(2, 'Operating System');
CALL Return_Book(3, 'Data Structures');
CALL Return_Book(4, 'Computer Networks');
CALL Return_Book(5, 'Database Systems');
CALL Return_Book(7, 'C++ Programming');
CALL Return_Book(10, 'Machine Learning');