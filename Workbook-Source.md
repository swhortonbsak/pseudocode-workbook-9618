# Pseudocode Workbook

Independent practice for Cambridge International Computer Science 9618

November 2026 • Original learning resource

Original independent practice; not endorsed by Cambridge International.

For notation, control-flow explanations, the worked trace and teacher notes, see build.py or the PDF.

## Core questions

### 1. School trip budget (5 marks)

Read a positive integer Students and a non-negative REAL TicketPrice. A coach costs 180.00 in total. Output the total trip cost and the cost per student, sharing the coach cost equally. You may assume the inputs have the stated types and ranges. Do not round the results.

Planning prompt: Add the coach charge once, before dividing by the number of students.

A dedicated full lined answer page follows this question in the PDF.

### 2. Parcel charge bands (6 marks)

Read a REAL Mass. If Mass is zero or negative, output Invalid mass. Otherwise charge 3.00 for a mass up to and including 1 kg, 5.50 for a mass above 1 kg and up to and including 5 kg, and 9.00 above 5 kg. Output only the applicable charge or the invalid message.

Planning prompt: Test the invalid range first, then put the remaining ranges in increasing order.

A dedicated full lined answer page follows this question in the PDF.

### 3. Three chances to unlock (7 marks)

A practice lock accepts the STRING code 2468. Read at most three code attempts. Stop asking as soon as an attempt is correct. Output Access granted after a correct attempt, or Locked after three incorrect attempts. Treat the code as text; each INPUT supplies one attempt.

Planning prompt: Track both the number of attempts and whether the lock is open.

A dedicated full lined answer page follows this question in the PDF.

### 4. Temperature log (8 marks)

Read INTEGER temperatures until 999 is entered. The value 999 is a sentinel and must not be processed. Output the average of the readings, or No readings if the sentinel is the first input. Valid readings may be positive, zero, or negative. Assume every non-sentinel input is a valid temperature.

Planning prompt: Read once before the loop and again at its end. Protect the division when no readings exist.

A dedicated full lined answer page follows this question in the PDF.

### 5. Seats still available (6 marks)

Read eight INTEGER values into FreeSeats[1:8]. Each value is the number of free seats on one minibus and is guaranteed to be from 0 to 15 inclusive. Output how many minibuses have at least four free seats, and output the total number of free seats across all eight minibuses.

Planning prompt: A count of qualifying buses and a sum of seats measure different things.

A dedicated full lined answer page follows this question in the PDF.

### 6. Mirror a message (6 marks)

Read a STRING Message, which may be empty. Build and output a second string containing the characters of Message in reverse order. Use LENGTH(S) for the number of characters and MID(S, Start, Count) for a substring; positions start at 1. Use & to concatenate strings. Do not call a built-in reverse function.

Planning prompt: Start with an empty result and visit the original positions from last to first.

A dedicated full lined answer page follows this question in the PDF.

### 7. Busiest activity row (8 marks)

Counts is an already populated INTEGER array with bounds [1:3,1:4]. Values are non-negative. Each row represents one activity and each column one session. Output each row total, then the row number with the largest total. If rows tie, choose the smallest row number. You do not need to read the array.

Planning prompt: Reset the row total inside the outer loop. A strict comparison preserves the first tied row.

A dedicated full lined answer page follows this question in the PDF.

### 8. First matching badge (7 marks)

Badges is an already populated STRING array with bounds [1:40]. N is an INTEGER from 0 to 40 giving the number of used entries. Read Target and output the index of its first occurrence within positions 1 to N, or 0 if it is absent. Repeated badge values are possible. Do not examine entries beyond N.

Planning prompt: Use position 0 for not found and stop the loop once it changes.

A dedicated full lined answer page follows this question in the PDF.

### 9. Sort waiting times (8 marks)

Times is an already populated INTEGER array with bounds [1:30]. N, from 1 to 30, gives its used length. Sort the used entries into ascending order using bubble sort. End early if a whole pass makes no swaps. Output each used value after sorting. Duplicate values must be retained.

Planning prompt: After one full pass, the largest remaining value is already in its final position.

A dedicated full lined answer page follows this question in the PDF.

### 10. Find a sorted catalogue code (8 marks)

Codes is an INTEGER array with bounds [1:100]. Its N used entries are already sorted in ascending order and contain distinct values; N is from 0 to 100. Read Target and use binary search to output its index, or 0 if absent. Do not sort the array or use linear search.

Planning prompt: Exclude the tested midpoint when narrowing the range.

A dedicated full lined answer page follows this question in the PDF.

### 11. A reusable common-factor function (7 marks)

Write a function CommonFactor(A : INTEGER, B : INTEGER) RETURNS INTEGER that returns the greatest common divisor of two positive integers. Use this method: repeatedly replace A by B and B by the remainder of the old A divided by the old B, stopping when B becomes zero. Also show a call for 84 and 30 that outputs the return value.

Planning prompt: Save the remainder before overwriting either value.

A dedicated full lined answer page follows this question in the PDF.

### 12. Select the best project (8 marks)

Define a record type ProjectRecord with a STRING Title, an INTEGER Score, and a BOOLEAN Submitted. Projects is an already populated array of 20 such records; N, from 0 to 20, gives the used length. Output the title and score of the submitted project with the highest score, or No submissions. Scores are 0 to 100. On a tie, use the first project in array order.

Planning prompt: Track the winning index; index 0 can represent no eligible project.

A dedicated full lined answer page follows this question in the PDF.

## Advanced questions

### 13. Recursive digit total (8 marks)

Write a recursive function DigitTotal(N : INTEGER) RETURNS INTEGER for N >= 0. It must return the sum of the decimal digits of N, without strings or loops. Use a base case for N < 10. Trace the calls and returned values for DigitTotal(5072). Explain why recursion terminates.

Planning prompt: Use N MOD 10 for the last digit and N DIV 10 for the remaining digits.

A dedicated full lined answer page follows this question in the PDF.

### 14. Safe stack removal (8 marks)

Stack is a global ARRAY[1:6] OF INTEGER and Top is a global INTEGER. Top = 0 means empty; otherwise Stack[Top] is the top item. Write Pop(BYREF Item : INTEGER, BYREF Success : BOOLEAN) as a procedure. If empty, set Success to FALSE and leave Item and Top unchanged. Otherwise copy the top item to Item, decrease Top, and set Success to TRUE. Show two calls when Top = 1 and Stack[1] = 42.

Planning prompt: Use the precondition 0 <= Top <= 6. Only access Stack[Top] after ruling out an empty stack.

A dedicated full lined answer page follows this question in the PDF.

### 15. Circular queue insertion (9 marks)

Queue is a global ARRAY[1:5] OF STRING. Global INTEGERs Front, Rear, and Count describe it: Front is the next item to remove, Rear is the next free slot to fill, and Count is the number stored. Initially Front = 1, Rear = 1, Count = 0. Write Enqueue(Value : STRING, BYREF Success : BOOLEAN). If full, report failure and change no queue state. Otherwise store Value, advance Rear with wraparound, increase Count, and report success. Enqueue must not change Front.

Planning prompt: For a wraparound trace, begin at Front = 4, Rear = 5, Count = 1 with Queue[4] = "old". Insert "new" and state the resulting pointers, count, and slot contents.

A dedicated full lined answer page follows this question in the PDF.

### 16. Build a reference-only file (9 marks)

The existing text file resources.txt contains one resource code per line. Copy every line beginning with the exact uppercase prefix REF- into a new text file reference.txt, in the same order. Ignore shorter and non-matching lines. Output the number copied. Handle an empty source file. You may assume file operations succeed. LENGTH(S) gives the length and MID(S, Start, Count) gives a substring from position 1.

Planning prompt: Check that a line has at least four characters before taking its four-character prefix. Opening reference.txt in WRITE mode replaces any existing contents.

A dedicated full lined answer page follows this question in the PDF.

## Final mark schemes and worked solutions

### 1. School trip budget (5 marks)

```text
DECLARE Students : INTEGER
DECLARE TicketPrice, TotalCost, CostEach : REAL
INPUT Students
INPUT TicketPrice
TotalCost ← Students * TicketPrice + 180.00
CostEach ← TotalCost / Students
OUTPUT TotalCost, CostEach
```

The multiplication accounts for every ticket. The fixed coach charge is then added to the total. Division produces a REAL result; Students cannot be zero under the question's precondition.

#### Test cases

- 30 students; ticket 12.50 → Total 555.00; per student 18.50
- 1 student; ticket 0.00 → Total 180.00; per student 180.00

#### Suggested marking points

- Suitable declarations and both inputs: 1 mark(s)
- Ticket cost multiplied by student count: 1 mark(s)
- Coach cost added once: 1 mark(s)
- Total divided by student count: 1 mark(s)
- Both results output: 1 mark(s)

Common error: Dividing only the ticket price by the number of students gives the wrong share of the total.

### 2. Parcel charge bands (6 marks)

```text
DECLARE Mass : REAL
INPUT Mass
IF Mass <= 0 THEN
   OUTPUT "Invalid mass"
ELSE
   IF Mass <= 1 THEN
      OUTPUT 3.00
   ELSE
      IF Mass <= 5 THEN
         OUTPUT 5.50
      ELSE
         OUTPUT 9.00
      ENDIF
   ENDIF
ENDIF
```

Each ELSE removes a range already considered. By the time Mass <= 5 is tested, Mass is known to be greater than 1. The nested branches ensure exactly one output.

#### Test cases

- Mass: 0, 1, 1.01 → Invalid mass; 3.00; 5.50
- Mass: 5, 5.01 → 5.50; 9.00

#### Suggested marking points

- Read Mass with a suitable type: 1 mark(s)
- Reject zero and negative masses: 1 mark(s)
- Correct inclusive 1 kg boundary: 1 mark(s)
- Correct inclusive 5 kg boundary: 1 mark(s)
- Correct remaining charge: 1 mark(s)
- Exactly one appropriate output: 1 mark(s)

Common error: Separate IF statements can print more than one price for the same mass.

### 3. Three chances to unlock (7 marks)

```text
DECLARE Attempt : STRING
DECLARE Attempts : INTEGER
DECLARE Unlocked : BOOLEAN
Attempts ← 0
Unlocked ← FALSE
WHILE (Attempts < 3) AND (Unlocked = FALSE)
   INPUT Attempt
   Attempts ← Attempts + 1
   IF Attempt = "2468" THEN
      Unlocked ← TRUE
   ENDIF
ENDWHILE
IF Unlocked THEN
   OUTPUT "Access granted"
ELSE
   OUTPUT "Locked"
ENDIF
```

The counter changes on every input, including a successful attempt. A successful third attempt is still accepted because the final message depends on Unlocked rather than the counter alone.

#### Test cases

- 2468 → One input; Access granted
- 1111, 0000, 2468 → Three inputs; Access granted
- a, b, c → Three inputs; Locked

#### Suggested marking points

- Counter and flag initialised: 1 mark(s)
- Loop enforces the three-attempt limit: 1 mark(s)
- Loop also stops after success: 1 mark(s)
- Input and counter update on each attempt: 1 mark(s)
- Compare with the correct STRING code: 1 mark(s)
- Update success flag: 1 mark(s)
- Correct final message: 1 mark(s)

Common error: Using Attempts = 3 to decide failure rejects a correct third attempt.

### 4. Temperature log (8 marks)

```text
DECLARE Reading, Total, Count : INTEGER
DECLARE Average : REAL
Total ← 0
Count ← 0
INPUT Reading
WHILE Reading <> 999
   Total ← Total + Reading
   Count ← Count + 1
   INPUT Reading
ENDWHILE
IF Count = 0 THEN
   OUTPUT "No readings"
ELSE
   Average ← Total / Count
   OUTPUT Average
ENDIF
```

Testing the sentinel before accumulation excludes it from both Total and Count. The empty-data branch avoids division by zero. Negative readings require no special case.

#### Test cases

- -4, 0, 10, 999 → Average 2.0
- 999 → No readings
- -8, 999 → Average -8.0

#### Suggested marking points

- Suitable declarations and zero initialisation: 1 mark(s)
- Initial input: 1 mark(s)
- Loop stops at 999: 1 mark(s)
- Accumulate valid values: 1 mark(s)
- Count valid values: 1 mark(s)
- Read the next value inside the loop: 1 mark(s)
- Handle zero readings: 1 mark(s)
- Calculate and output the average: 1 mark(s)

Common error: Counting 999 as a reading changes both the numerator and the denominator.

### 5. Seats still available (6 marks)

```text
DECLARE FreeSeats : ARRAY[1:8] OF INTEGER
DECLARE Index, Suitable, Total : INTEGER
Suitable ← 0
Total ← 0
FOR Index ← 1 TO 8
   INPUT FreeSeats[Index]
   Total ← Total + FreeSeats[Index]
   IF FreeSeats[Index] >= 4 THEN
      Suitable ← Suitable + 1
   ENDIF
NEXT Index
OUTPUT Suitable, Total
```

Every input contributes its seat value to Total. Only inputs meeting the inclusive threshold contribute one to Suitable. All eight array positions are visited exactly once.

#### Test cases

- 0, 4, 7, 3, 15, 4, 1, 2 → 4 qualifying buses; 36 free seats
- 0, 0, 0, 0, 0, 0, 0, 0 → 0 qualifying buses; 0 free seats

#### Suggested marking points

- Correct array declaration: 1 mark(s)
- Both accumulators initialised: 1 mark(s)
- Loop reads all eight elements: 1 mark(s)
- Accumulate seat values: 1 mark(s)
- Count values >= 4: 1 mark(s)
- Output both results: 1 mark(s)

Common error: Suitable must increase by one per qualifying bus, rather than by its seat count.

### 6. Mirror a message (6 marks)

```text
DECLARE Message, Mirrored : STRING
DECLARE Position : INTEGER
INPUT Message
Mirrored ← ""
FOR Position ← LENGTH(Message) TO 1 STEP -1
   Mirrored ← Mirrored & MID(Message, Position, 1)
NEXT Position
OUTPUT Mirrored
```

Each substring contains one character. For an empty input the starting position is zero, so the negative-step loop has no iterations and the result stays empty.

#### Test cases

- Code! → !edoC
- a → a
- Empty string → Empty string

#### Suggested marking points

- Suitable declarations and input: 1 mark(s)
- Empty result initialised: 1 mark(s)
- Start at the final character: 1 mark(s)
- Move backwards to position 1: 1 mark(s)
- Extract and concatenate one character: 1 mark(s)
- Output the reversed string: 1 mark(s)

Common error: Using + instead of & treats string joining like arithmetic.

### 7. Busiest activity row (8 marks)

```text
// Counts is supplied with bounds [1:3,1:4]
DECLARE Row, Column, RowTotal : INTEGER
DECLARE BestRow, BestTotal : INTEGER
BestRow ← 1
BestTotal ← -1
FOR Row ← 1 TO 3
   RowTotal ← 0
   FOR Column ← 1 TO 4
      RowTotal ← RowTotal + Counts[Row, Column]
   NEXT Column
   OUTPUT RowTotal
   IF RowTotal > BestTotal THEN
      BestTotal ← RowTotal
      BestRow ← Row
   ENDIF
NEXT Row
OUTPUT BestRow
```

Because all entries are non-negative, -1 is below every possible row total. Updating only for a strictly greater total keeps the earlier row in a tie.

#### Test cases

- Rows: [1,2,3,4]; [5,0,5,0]; [0,2,0,1] → Totals 10, 10, 3; best row 1
- All twelve values are 0 → Totals 0, 0, 0; best row 1

#### Suggested marking points

- Valid initial best row and total: 1 mark(s)
- Outer loop covers three rows: 1 mark(s)
- Reset RowTotal for each row: 1 mark(s)
- Inner loop covers four columns: 1 mark(s)
- Correct 2D indexing and accumulation: 1 mark(s)
- Output each row total: 1 mark(s)
- Update total and row while preserving ties: 1 mark(s)
- Output the winning row number: 1 mark(s)

Common error: Resetting RowTotal before the outer loop produces running totals across rows.

### 8. First matching badge (7 marks)

```text
// Badges and N are supplied
DECLARE Target : STRING
DECLARE Index, Position : INTEGER
INPUT Target
Index ← 1
Position ← 0
WHILE (Index <= N) AND (Position = 0)
   IF Badges[Index] = Target THEN
      Position ← Index
   ENDIF
   Index ← Index + 1
ENDWHILE
OUTPUT Position
```

The loop condition contains no array access. Consequently no assumption about short-circuit Boolean evaluation is needed to keep the array access safe. For N = 0, the body is skipped.

#### Test cases

- Used badges A, C, A; Target A → 1
- Used badges A, C, A; Target Z → 0
- N = 0; any Target → 0

#### Suggested marking points

- Read Target and initialise search state: 1 mark(s)
- Loop stays within used entries: 1 mark(s)
- Loop stops after the first match: 1 mark(s)
- Compare the current badge: 1 mark(s)
- Save its index: 1 mark(s)
- Advance the index: 1 mark(s)
- Correct output for found and absent targets: 1 mark(s)

Common error: Continuing and overwriting Position on every match returns the last match.

### 9. Sort waiting times (8 marks)

```text
// Times and N are supplied
DECLARE Last, Index, Temp : INTEGER
DECLARE Swapped : BOOLEAN
Last ← N
Swapped ← TRUE
WHILE (Last > 1) AND Swapped
   Swapped ← FALSE
   FOR Index ← 1 TO Last - 1
      IF Times[Index] > Times[Index + 1] THEN
         Temp ← Times[Index]
         Times[Index] ← Times[Index + 1]
         Times[Index + 1] ← Temp
         Swapped ← TRUE
      ENDIF
   NEXT Index
   Last ← Last - 1
ENDWHILE
FOR Index ← 1 TO N
   OUTPUT Times[Index]
NEXT Index
```

Each pass moves the largest unsorted value to Last. The next pass excludes that position. A pass without swaps proves that the remaining prefix is in order.

#### Test cases

- Used values 9, 3, 3, 1 → 1, 3, 3, 9
- Used value 5 → 5; no comparison needed
- Used values 1, 2, 3 → 1, 2, 3; first pass makes no swaps

#### Suggested marking points

- Initialise pass state: 1 mark(s)
- Reset swap flag each pass: 1 mark(s)
- Correct adjacent comparison bounds: 1 mark(s)
- Compare in ascending-order direction: 1 mark(s)
- Correct three-assignment swap: 1 mark(s)
- Set flag after a swap: 1 mark(s)
- Shrink the bound and stop when sorted: 1 mark(s)
- Output all used entries: 1 mark(s)

Common error: Comparing up to Last accesses Times[Last + 1], outside the active region.

### 10. Find a sorted catalogue code (8 marks)

```text
// Codes and N are supplied
DECLARE Target, Low, High, Mid, Position : INTEGER
INPUT Target
Low ← 1
High ← N
Position ← 0
WHILE (Low <= High) AND (Position = 0)
   Mid ← (Low + High) DIV 2
   IF Codes[Mid] = Target THEN
      Position ← Mid
   ELSE
      IF Codes[Mid] < Target THEN
         Low ← Mid + 1
      ELSE
         High ← Mid - 1
      ENDIF
   ENDIF
ENDWHILE
OUTPUT Position
```

Low and High describe an inclusive search interval. Removing Mid after a failed comparison guarantees progress. An empty array starts with Low > High and needs no special array access.

#### Test cases

- Codes 4, 9, 15, 22; Target 22 → 4
- Codes 4, 9, 15, 22; Target 10 → 0
- N = 0; any Target → 0

#### Suggested marking points

- Read target and initialise bounds: 1 mark(s)
- Initialise absent-result state: 1 mark(s)
- Correct loop termination: 1 mark(s)
- Integer midpoint: 1 mark(s)
- Record a successful match: 1 mark(s)
- Correct lower-bound update: 1 mark(s)
- Correct upper-bound update: 1 mark(s)
- Output found index or 0: 1 mark(s)

Common error: Low ← Mid can repeat the same midpoint forever when the interval is small.

### 11. A reusable common-factor function (7 marks)

```text
FUNCTION CommonFactor(A : INTEGER, B : INTEGER)
   RETURNS INTEGER
   DECLARE Remainder : INTEGER
   WHILE B <> 0
      Remainder ← A MOD B
      A ← B
      B ← Remainder
   ENDWHILE
   RETURN A
ENDFUNCTION

OUTPUT CommonFactor(84, 30)
```

The nonzero remainders decrease until B becomes zero. At that point A holds the greatest common divisor. The parameters are passed by value, so this function does not change the caller's variables.

#### Test cases

- 84, 30 → 6
- 7, 7 → 7
- 13, 5 → 1

#### Suggested marking points

- Function header with typed parameters and return type: 1 mark(s)
- Loop stops when B is zero: 1 mark(s)
- Calculate A MOD B before overwriting: 1 mark(s)
- Replace A with old B: 1 mark(s)
- Replace B with the saved remainder: 1 mark(s)
- RETURN A: 1 mark(s)
- Correct output of a function call: 1 mark(s)

Common error: OUTPUT inside the function is not a substitute for returning a value to its caller.

### 12. Select the best project (8 marks)

```text
TYPE ProjectRecord
   DECLARE Title : STRING
   DECLARE Score : INTEGER
   DECLARE Submitted : BOOLEAN
ENDTYPE
// Supplied: Projects : ARRAY[1:20] OF ProjectRecord
// Supplied: N : INTEGER
DECLARE Index, BestIndex, BestScore : INTEGER
BestIndex ← 0
BestScore ← -1
FOR Index ← 1 TO N
   IF Projects[Index].Submitted THEN
      IF Projects[Index].Score > BestScore THEN
         BestScore ← Projects[Index].Score
         BestIndex ← Index
      ENDIF
   ENDIF
NEXT Index
IF BestIndex = 0 THEN
   OUTPUT "No submissions"
ELSE
   OUTPUT Projects[BestIndex].Title,
          Projects[BestIndex].Score
ENDIF
```

BestScore = -1 is safe because valid scores are non-negative. The best index remains zero when no submitted project is visited. Strictly greater comparison preserves the first eligible project on a tie.

#### Test cases

- (Map,70,FALSE), (Game,60,TRUE), (Art,60,TRUE) → Game, 60
- N = 0, or all Submitted = FALSE → No submissions

#### Suggested marking points

- Record type with all three fields and types: 1 mark(s)
- Initialise best-index and best-score state: 1 mark(s)
- Visit only the N used records: 1 mark(s)
- Ignore unsubmitted projects: 1 mark(s)
- Correct comparison preserving first tie: 1 mark(s)
- Update both winning fields: 1 mark(s)
- Handle no submissions: 1 mark(s)
- Output winning title and score: 1 mark(s)

Common error: Selecting the largest score before checking Submitted can choose an ineligible project.

### 13. Recursive digit total (8 marks)

```text
FUNCTION DigitTotal(N : INTEGER) RETURNS INTEGER
   IF N < 10 THEN
      RETURN N
   ELSE
      RETURN (N MOD 10) + DigitTotal(N DIV 10)
   ENDIF
ENDFUNCTION
```

Calls descend through 5072, 507, 50, and 5. The base call returns 5. Unwinding gives 0 + 5 = 5, then 7 + 5 = 12, then 2 + 12 = 14. For each recursive call with N >= 10, integer division by 10 produces a smaller non-negative integer; it eventually reaches a single digit.

#### Test cases

- DigitTotal(0) → 0
- DigitTotal(5072) → 14
- DigitTotal(999) → 27

#### Suggested marking points

- Typed recursive function signature: 1 mark(s)
- Correct single-digit base condition: 1 mark(s)
- Base case returns N: 1 mark(s)
- Extract final digit using MOD: 1 mark(s)
- Recursive call on N DIV 10: 1 mark(s)
- Return the sum: 1 mark(s)
- Correct call and return trace for 5072: 1 mark(s)
- Termination explained using a decreasing input: 1 mark(s)

Common error: Calling DigitTotal(N) again leaves the argument unchanged and never reaches the base case.

### 14. Safe stack removal (8 marks)

```text
PROCEDURE Pop(BYREF Item : INTEGER,
              BYREF Success : BOOLEAN)
   IF Top = 0 THEN
      Success ← FALSE
   ELSE
      Item ← Stack[Top]
      Top ← Top - 1
      Success ← TRUE
   ENDIF
ENDPROCEDURE

DECLARE Value : INTEGER
DECLARE OK : BOOLEAN
CALL Pop(Value, OK)
OUTPUT Value, OK
CALL Pop(Value, OK)
OUTPUT Value, OK
```

Starting from the specified state, the first call outputs 42, TRUE and leaves Top = 0. The second outputs 42, FALSE and leaves Top = 0. Value retains its earlier value after the failed call. BYREF allows Item and Success to update the variables passed by the caller. Global Stack and Top are supplied state, so no local redeclarations are needed.

#### Test cases

- Top 1; Stack[1] 42; two pops → (42, TRUE), then (42, FALSE)
- Top 0; Item initially 9 → Item 9; Success FALSE; Top 0

#### Suggested marking points

- Procedure with both BYREF parameters: 1 mark(s)
- Check empty before array access: 1 mark(s)
- Report failure on empty: 1 mark(s)
- Preserve Item and Top on empty: 1 mark(s)
- Read the current top item: 1 mark(s)
- Decrease Top and report success: 1 mark(s)
- Two correctly formed procedure calls: 1 mark(s)
- Correct state and outputs for both calls: 1 mark(s)

Common error: Decreasing Top before reading the item removes the wrong element and can access index 0.

### 15. Circular queue insertion (9 marks)

```text
PROCEDURE Enqueue(Value : STRING,
                  BYREF Success : BOOLEAN)
   IF Count = 5 THEN
      Success ← FALSE
   ELSE
      Queue[Rear] ← Value
      Rear ← Rear + 1
      IF Rear > 5 THEN
         Rear ← 1
      ENDIF
      Count ← Count + 1
      Success ← TRUE
   ENDIF
ENDPROCEDURE
```

Rear always identifies the next insertion slot. With Front = 4, Rear = 5 and Count = 1, insertion writes new to Queue[5], wraps Rear to 1, and makes Count = 2. Front stays 4 and Queue[4] stays old. With Count = 5 the failure branch performs no writes to Queue, Front, Rear, or Count.

#### Test cases

- Rear 5; Count 1; insert new → Queue[5] new; Rear 1; Count 2; success
- Count 5; any insertion → Failure; all queue state unchanged

#### Suggested marking points

- Typed procedure and BYREF status: 1 mark(s)
- Correct full condition: 1 mark(s)
- Failure status without changing queue state: 1 mark(s)
- Store at the current Rear: 1 mark(s)
- Advance Rear: 1 mark(s)
- Wrap from 6 to 1: 1 mark(s)
- Increase Count and report success: 1 mark(s)
- Preserve Front: 1 mark(s)
- Correct wraparound trace: 1 mark(s)

Common error: Front = Rear can describe either empty or full here; Count distinguishes those states.

### 16. Build a reference-only file (9 marks)

```text
DECLARE Line : STRING
DECLARE Copied : INTEGER
Copied ← 0
OPENFILE "resources.txt" FOR READ
OPENFILE "reference.txt" FOR WRITE
WHILE NOT EOF("resources.txt")
   READFILE "resources.txt", Line
   IF LENGTH(Line) >= 4 THEN
      IF MID(Line, 1, 4) = "REF-" THEN
         WRITEFILE "reference.txt", Line
         Copied ← Copied + 1
      ENDIF
   ENDIF
ENDWHILE
CLOSEFILE "resources.txt"
CLOSEFILE "reference.txt"
OUTPUT Copied
```

EOF is checked before each read, including the first one, so an empty input produces an empty output file and a count of zero. The nested length check keeps the substring call valid without depending on short-circuit evaluation. Writing immediately preserves the source order.

#### Test cases

- Lines: REF-7, AB, ref-8, REF-2 → Output lines REF-7, REF-2; count 2
- Empty source file → Empty output file; count 0
- Line REF- → Line copied; count 1

#### Suggested marking points

- Open input for READ and output for WRITE: 1 mark(s)
- Initialise count and use STRING line storage: 1 mark(s)
- EOF tested before reading: 1 mark(s)
- Read each source line once: 1 mark(s)
- Guard substring with a length check: 1 mark(s)
- Test the exact uppercase prefix: 1 mark(s)
- Write matches and increase count: 1 mark(s)
- Close both files: 1 mark(s)
- Output count, including zero for empty input: 1 mark(s)

Common error: APPEND mode retains old output, so rerunning the program would duplicate earlier results.
