%% Data Visual of 911 Emergencies Throughout the Day
date = [0:1:23];
frequency = [304,283,304,205,224,193,256,303,348,502,517,511,588,506,536,577,595,503,521,549,487,383,441,364];



figure(1);
plot(date,frequency,'*');
xlabel('Military Time, T, hr');
ylabel('Frequency, f, n');
title('Military Time vs. Frequency of 911 Emergencies from 1/13-1/24 in SF');

conLin = polyfit(date, frequency, 1);

mBFL = conLin(1);
kBFL = conLin(2);
yBFL = (mBFL.*date) + kBFL;
hold on
%plot(date, yBFL);



