var a, b, c, x1, x2: real;
var input: string;

begin
  writeln('Введите коэффициенты уравнения:');
  
  repeat
    write('a = ');
    readln(input);
  until TryStrToFloat(input, a);
  repeat
    write('b = ');
    readln(input);
  until TryStrToFloat(input, b);
  repeat
    write('c = ');
    readln(input);
  until TryStrToFloat(input, c);

if (a=0) then begin
    writeln('Уравнение не является биквадратным.');
    halt;
    end;
    
    if (b*b-4*a*c>0) then
    begin
      x1 := (-b+sqrt(b*b-4*a*c))/(2*a);
      x2 := (-b-sqrt(b*b-4*a*c))/(2*a);
      writeln('Уравнение имеет два корня:');
      writeln('x1 = ', x1);
      writeln('x2 = ', x2);
    end;
    
    if (b*b-4*a*c=0) then
    begin
      x1 := (-b+sqrt(b*b-4*a*c))/(2*a);
      writeln('Уравнение имеет один корень:');
      writeln('x1 = ', x1);      
    end;
    
    if (b*b-4*a*c<0) then
      writeln('Уравнение не имеет действительных корней');

    {if (a=0) then
    writeln('Уравнение не является биквадратным. a<>0');}
    
  readln;
end.