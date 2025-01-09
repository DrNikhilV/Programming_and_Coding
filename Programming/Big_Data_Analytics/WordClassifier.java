import java.io.IOException;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class WordClassifier {
    public static class WordMapper extends Mapper<Object, Text, Text, IntWritable> {
        private final static Text small = new Text("Small");
        private final static Text medium = new Text("Medium");
        private final static Text large = new Text("Large");

        public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
            String[] words = value.toString().split("\\s+");
            for (String word : words) {
                int length = word.length();
                if (length >= 1 && length <= 3) {
                    context.write(small, new IntWritable(1));
                } else if (length >= 4 && length <= 7) {
                    context.write(medium, new IntWritable(1));
                } else if (length >= 8) {
                    context.write(large, new IntWritable(1));
                }
            }
        }
    }

    public static class WordReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
        public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
            int sum = 0;
            for (IntWritable val : values) {
                sum += val.get();
            }
            context.write(key, new IntWritable(sum));
        }
    }

    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "word classifier");
        job.setJarByClass(WordClassifier.class);
        job.setMapperClass(WordMapper.class);
        job.setCombinerClass(WordReducer.class);
        job.setReducerClass(WordReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
