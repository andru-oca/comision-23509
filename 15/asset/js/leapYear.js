function leapYear(year) {
  if (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0)) {
    return true;
  }

  return false;
}

const leapYearNewWave = (year) =>
  year % 400 == 0 || (year % 4 == 0 && year % 100 != 0);

export { leapYear, leapYearNewWave };
