function levenshtein(word1,word2: string): integer;
var matrix: array of array of integer;
var i, j, cost: integer;
begin
  SetLength(matrix, Length(word1) + 1);
for i := 0 to Length(word1) do
  SetLength(matrix[i], Length(word2) + 1);
  
  for i := 0 to Length(word1) do
    matrix[i][0] := i;
  
  for j := 0 to Length(word2) do
    matrix[0][j] := j;
  
  for i := 1 to Length(word1) do
  begin
    for j := 1 to Length(word2) do
    begin
      if word1[i] = word2[j] then
        cost := 0
      else
        cost := 1;
      
      matrix[i][j] := Min(Min(
        matrix[i - 1][j] + 1,      // удаление
        matrix[i][j - 1] + 1),      // вставка
        matrix[i - 1][j - 1] + cost // замена
      );
    end;
  end;
  
  Result := matrix[Length(word1)][Length(word2)];
end;

var word1, word2: string;
var distance: integer;
begin
  Write('Введите первое слово: ');
  Readln(word1);
  
  Write('Введите второе слово: ');
  Readln(word2);
  
  distance := levenshtein(word1, word2);
  WriteLn('Расстояние Левенштейна равно:', distance);
end.