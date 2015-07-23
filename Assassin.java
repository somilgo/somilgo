import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class Assassin 
{

	public final static String fileLoc = "C:\\Users\\Govani\\Documents\\Somil\\Assassin\\targets.csv";
	public static void main(String[] args) throws IOException 
	{
		String csvFile = "C:/Users/Govani/Documents/Somil/Assassin/test.csv";
		BufferedReader br = new BufferedReader(new FileReader(csvFile));
		String line = "";
		ArrayList<String> tempAss = new ArrayList<String>();
		
		while ((line = br.readLine()) != null)
		{
			String[] lineRead = line.split(",");
			for (String l : lineRead)
			{
				tempAss.add(l);
			}
		}
		
		String [] assassins = new String[tempAss.size()];
		for (int p = 0; p < tempAss.size(); p++)
		{
			assassins[p] = tempAss.get(p);
		}
		//String[] assassins = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10"};
		ArrayList<String> targets = new ArrayList<String>();
		ArrayList<String> possTargets = new ArrayList<String>();
		for (String x : assassins)
		{
			possTargets.add(x);
		}
		int randInd = 0;
		int partInd = 1;
		int exCount = 0;
		String cannotBe = "filler";
		String target = "";
		int assTar = 0;
		boolean partnerAssigned = false;
		
		for (int i = 0; i < assassins.length; i++)
		{
			if (i % 2 == 1) {partInd = i - 1; partnerAssigned = true;}
			else {partInd = i + 1; partnerAssigned = false;}
			randInd = (int) (Math.random() * possTargets.size());
			exCount = 0;
			
			while (((possTargets.get(randInd).equals(assassins[partInd])) || (possTargets.get(randInd).equals(assassins[i])) || (possTargets.get(randInd).equals(cannotBe)) || checkRecip(randInd, i, possTargets, assassins, targets)) && exCount < 100 )
			{
				randInd = (int) (Math.random() * possTargets.size());
				exCount++;
				if (exCount >= 100) {System.out.println("retry");}
			}
			
			target = possTargets.get(randInd);
			targets.add(target);
			assTar = java.util.Arrays.asList(assassins).indexOf(target);
			
			if (i % 2 != 1 && assTar % 2 != 1){cannotBe = assassins[assTar + 1];}
			else if (i % 2 != 1 && assTar % 2 == 1){cannotBe = assassins[assTar - 1];}
			else {cannotBe = "filler";}
			possTargets.remove(randInd);
		}
		
		for (int j = 0; j < assassins.length; j++)
		{
			System.out.print(assassins[j] + "\t" + "\t");
			System.out.println(targets.get(j));
		}
		
		try
		{
		    FileWriter writer = new FileWriter(fileLoc);
		    
		   
		    
		    for (int i = 0; i < assassins.length; i+=2)
		    {
		    	writer.append(assassins[i] + ",");
		    	writer.append(assassins[i+1] + ",");
		    	writer.append(targets.get(i) + ",");
		    	writer.append(targets.get(i+1));
		    	writer.append("\n");
		    }	
		    
		    writer.flush();
		    writer.close();
		}
		catch(IOException e)
		{
		     e.printStackTrace();
		} 

	}
	
	public static boolean checkRecip (int rand, int ind, ArrayList<String> possTargets, String[] killers, ArrayList<String> targets)
	{
		int partInde = 0;
		int partInd2 = 0;
		String potTar = possTargets.get(rand);
		int assInd = java.util.Arrays.asList(killers).indexOf(potTar);
		if (assInd % 2 == 1) {partInde = assInd - 1;}
		else {partInde = assInd + 1;}
		if (ind % 2 == 1) {partInd2 = ind - 1;}
		else {partInd2 = ind + 1;}
		if (assInd < targets.size() && killers[ind].equals(targets.get(assInd)))
		{
			return true;
		}
		else if (partInde < targets.size() && killers[ind].equals(targets.get(partInde)))
		{
			return true;
		}
		else if (partInde < targets.size() && killers[partInd2].equals(targets.get(partInde)))
		{
			return true;
		}
		else if (assInd < targets.size() && killers[partInd2].equals(targets.get(assInd)))
		{
			return true;
		}
		
		else
		{
			return false;
		}
		
	}

}
