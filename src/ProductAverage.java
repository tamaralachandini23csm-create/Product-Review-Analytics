import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class ProductAverage {

    public static class RatingMapper
            extends Mapper<LongWritable, Text, Text, LongWritable> {

        public void map(LongWritable key, Text value, Context context)
                throws IOException, InterruptedException {

            String[] fields = value.toString().split("\t", -1);

            if (fields.length == 4) {
                try {
                    String productId = fields[0];
                    long rating = Long.parseLong(fields[3]);

                    context.write(new Text(productId),
                                  new LongWritable(rating));

                } catch (NumberFormatException e) {
                    // Skip invalid ratings
                }
            }
        }
    }

    public static class RatingReducer
            extends Reducer<Text, LongWritable, Text, Text> {

        public void reduce(Text key, Iterable<LongWritable> values,
                           Context context)
                throws IOException, InterruptedException {

            long sum = 0;
            long count = 0;

            for (LongWritable value : values) {
                sum += value.get();
                count++;
            }

            double average = (double) sum / count;

            context.write(key, new Text(
                String.format("%.2f\t%d", average, count)
            ));
        }
    }

    public static void main(String[] args) throws Exception {

        Configuration conf = new Configuration();

        Job job = Job.getInstance(conf, "Product Average Rating");

        job.setJarByClass(ProductAverage.class);

        job.setMapperClass(RatingMapper.class);
        job.setReducerClass(RatingReducer.class);

        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(LongWritable.class);

        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
