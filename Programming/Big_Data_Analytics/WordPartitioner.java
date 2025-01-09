import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import java.io.IOException;
import java.util.StringTokenizer;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Partitioner;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.util.GenericOptionsParser;

/* Use the input file lower_upper for running this program */
/*To understand the partitioner,refer the following link  http://www.hadooptpoint.com/hadoop-custom-partitioner-in-mapreduce-example/#codesyntax_2 */
public class WordPartitioner {
public static class WordMap extends Mapper<LongWritable, Text, Text, IntWritable> {
    private final IntWritable one = new IntWritable(1);
    private Text word = new Text();
    public void map(LongWritable key,Text value,Context context)throws IOException,InterruptedException{
        StringTokenizer itr = new StringTokenizer(value.toString());
        while (itr.hasMoreTokens()) {
            word.set(itr.nextToken());
            context.write(word, one);
        }
    }

}
 
/*getPartition() method is responsible to partition the output of map() and send the keys which start with lowercase alphabet to reducer1 and the keys which start with uppercase alphabet to reducer2. So, number of output files will be 2 */
public static class Wordpartitioner extends Partitioner<Text, IntWritable> {
    String partititonkey;
    @Override
    public int getPartition(Text key, IntWritable value, int numPartitions) {
        if(numPartitions == 2){
            String partitionKey = key.toString(); //mango.toString() //Apple
            if(partitionKey.charAt(0) >='a' ) //if(100>=97)
                return 0; //send plum to reducer 0 (Reducer1)
            else
                return 1; //send Apple to reducer 1(Reducer2)
        } else if(numPartitions == 1)
            return 0;
        else{
            System.err.println("WordCountParitioner can only handle either 1 or 2 paritions");
            return 0;
        }
    }

}

public static class Wordreduce extends Reducer<Text, IntWritable, Text, IntWritable>{
    public void reduce(Text key,Iterable<IntWritable> values,Context context)throws IOException,InterruptedException{
        IntWritable result = new IntWritable();
        int sum = 0;
        for (IntWritable val : values) {
        sum += val.get();
        result.set(sum);
        }
        context.write(key, result);
    }

}
    public static void main(String[] args)throws Exception {
        Configuration conf = new Configuration();
        String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
            if (otherArgs.length != 2) {
      System.err.println("Usage: wordcount <in> <out>");
      System.exit(2);
    }

        Job job = new Job(conf,"WordPartitioner");
        job.setJarByClass(WordPartitioner.class);
        job.setMapperClass(WordMap.class);
        job.setReducerClass(Wordreduce.class);
        job.setMapOutputKeyClass(Text.class);
        job.setPartitionerClass(Wordpartitioner.class); //This is partitioner class
        job.setNumReduceTasks(2); //This will create two reduce tasks  //2 reducers. 1st reducer is identified with reduce 0 and identifier of the second reducer is reduce1. those unique words start with lower case alphabet to be aggregated/processed by reduce 0 and those unique words start with upper case alphabet to be aggregated/processed by reduce 1
        
        job.setMapOutputValueClass(IntWritable.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        System.exit(job.waitForCompletion(true) ? 0:1 );


    }

}
