import java.io.IOException;
import java.util.StringTokenizer;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.JobConf;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

public class WordCountCombiner {

  public static class TokenizerMapper 
       extends Mapper<Object, Text, Text, IntWritable>{
    /* In the above line, the Object indicates offset(position of the text in the file) within the file. The first Text indicates the content of the line, The second Text indicates each word from a line of the file. IntWritable indicates value 1 */ 
    /* the int equivalent of java in hadoop is IntWritable. The 1 in IntWritable constructor indicates that along with every output word, 1 has to printed */
    private final static IntWritable one = new IntWritable(1);
//Integer one = new Integer(1)
    //Text class stores text using standard UTF8 encoding
    private Text word = new Text();  
      //String word = new String();
    public void map(Object key, Text value, Context context
    ) throws IOException, InterruptedException {
   //System.out.println(key+" "+value.toString());
    /* the following three lines of code extracts every word from every line */
      StringTokenizer itr = new StringTokenizer(value.toString());
     // System.out.println(itr);
      while (itr.hasMoreTokens()) {
        word.set(itr.nextToken());
      /* The following line prints word with 1. It is like System.out.println. */
        context.write(word, one);
      }
    }
  }
  

  public static class IntSumReducer 
       extends Reducer<Text,IntWritable,Text,IntWritable> {
    
    private IntWritable result = new IntWritable();

    /* In the following line, the first argument indicates a word in the input file. The second argument indicates a list of values. For example, consider "Apple" is a word in the input file and it occurs 5 times. Then, map function  gives this (Apple,[1,1,1,1]) as an output for the word "Apple". [1,1,1,1] is an iterable list. mango,[1,1] */

    public void reduce(Text key, Iterable<IntWritable> values, 
                       Context context
                       ) throws IOException, InterruptedException {
      int sum = 0;
      /* The following is "for each" loop */
      for (IntWritable val : values) {
        sum += val.get(); 
      }
      result.set(sum);
      context.write(key, result);
    }
  }

 
  public static void main(String[] args) throws Exception {
    
    /* The following line will create configuration object “conf” and it will provide access to configuration parameters. Configuration parameters are defined in the form of xml data and by default, Hadoop specifies two configuration files. 2 configuration files are core-default.xml and core-site.xml*/

    Configuration conf = new Configuration();  

    /* GenericOptionsParser is to read command line arguments which are generic to the Hadoop framework and application-specific arguments. With the help of getRemainingArgs() method, we are retrieving an array of Strings containing only application-specific arguments. otherArgs will have the path of input directory where our input files are stored and output directory where output will be stored */

    String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
   
    /* The following if block is to check whether input and output folders are mentioned in the command line arguments or not */

    if (otherArgs.length != 2) {
      System.err.println("Usage: wordcount <in> <out>");
      System.exit(2);
    }

    /* The Job class allows the user to configure the job, submit it and control its execution. As a user, we create the application(for example Word Count Program), describes various facets of the job via Job class and then submits the job and monitor its progress.When the following line is executed, it will create a new Job with the given name (word count) and with default configurations provided by “conf” object */   
        
    Job job = new Job(conf, "word count");
    job.setJarByClass(WordCountCombiner.class);
    job.setMapperClass(TokenizerMapper.class);
    job.setCombinerClass(IntSumReducer.class); 
    job.setReducerClass(IntSumReducer.class);
 
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(IntWritable.class);

    /* In the above code, Please note that we are only setting Output key and Output Value data types in the above section. Input key and Input Value data types are specified in the Mapper & Reducer classes.*/


    
/* addInputPath is a method of FileInputFormat class and it is used to add a Path to the list of inputs for the map-reduce job. FileInputFormat is an abstract class and is the base class of InputFormats. Because abstract classes can not be instantiated, we used classname.method() format to invoke the particular method*/

    FileInputFormat.addInputPath(job, new Path(otherArgs[0]));
    /* setOutputPath is a method of FileOutputFormat class and it is used to define the output directory.*/

    FileOutputFormat.setOutputPath(job, new Path(otherArgs[1]));

    /* wait till job completion*/
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}


