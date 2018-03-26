

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Hashtable;

public class Daily911CallFreq {

    public static void main(String[] args) throws IOException {

        String csvFile =
            "C:\\Users\\khann\\Desktop\\CapitalOne Summit\\sfpd-dispatch\\sfpd_dispatch_data_subset.csv";
        BufferedReader reader = null;
        String line = "";

        Hashtable<String, Integer> dayFreq = new Hashtable<String, Integer>();

        String tstamp = "";

        try {

            reader = new BufferedReader(new FileReader(csvFile));
            while ((line = reader.readLine()) != null) {

                // use comma as separator
                String[] data = line.split(",");
                tstamp = data[6].substring(11, 13);

                if (dayFreq.containsKey(tstamp)) {
                    dayFreq.put(tstamp, dayFreq.get(tstamp) + 1);
                }
                else {
                    dayFreq.put(tstamp, 1);
                }

            }

            System.out.println(dayFreq);

        }

        finally {
            if (reader != null) {
                try {
                    reader.close();
                }
                catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }

    }

}
